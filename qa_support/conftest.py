"""Pytest plugin for running variant solutions in isolated temporary directories."""

import ast
import os
import subprocess
import sys

import pytest


_FIXED_RANDOM = """
import ast
import random
import runpy
import sys
from unittest.mock import patch

script = sys.argv[1]
values = iter(ast.literal_eval(sys.argv[2]))
sys.argv = [script, *sys.argv[3:]]

with patch.object(random.Random, "randint", side_effect=lambda low, high: next(values)):
    runpy.run_path(script, run_name="__main__")
"""


def _replace_assignments(source, replacements):
    tree = ast.parse(source)
    remaining = dict(replacements)
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in remaining:
                node.value = ast.parse(repr(remaining.pop(target.id)), mode="eval").body
    if remaining:
        raise ValueError(f"Missing top-level assignments: {', '.join(remaining)}")
    return ast.unparse(ast.fix_missing_locations(tree)) + "\n"


@pytest.fixture
def variant_directory(request):
    return request.path.parent.parent


@pytest.fixture
def solution_path(variant_directory):
    def find(level):
        path, = (variant_directory / "src").glob(f"*_({level}).py")
        return path

    return find


@pytest.fixture
def run_solution(solution_path, tmp_path):
    def run(level, *, inputs=None, args=(), files=None, assignments=None, fixed_values=None):
        src = solution_path(level)
        source_directory = tmp_path / "src"
        source_directory.mkdir(exist_ok=True)
        script = source_directory / src.name
        if assignments is None:
            script.write_bytes(src.read_bytes())
        else:
            code = src.read_text(encoding="utf-8")
            script.write_text(_replace_assignments(code, assignments), encoding="utf-8")
        for name, content in (files or {}).items():
            (tmp_path / name).write_text(content, encoding="utf-8")

        command = [str(script), *args]
        if fixed_values is not None:
            command = ["-c", _FIXED_RANDOM, str(script), repr(list(fixed_values)), *args]
        input_options = (
            {"stdin": subprocess.DEVNULL}
            if inputs is None
            else {"input": "".join(f"{value}\n" for value in inputs)}
        )
        return subprocess.run(
            [sys.executable, *command],
            cwd=tmp_path,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            encoding="utf-8",
            capture_output=True,
            timeout=15,
            check=False,
            **input_options,
        )

    return run


@pytest.fixture
def assert_noob_source(solution_path):
    def check():
        tree = ast.parse(solution_path("noob").read_text(encoding="utf-8"))
        forbidden = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda, ast.JoinedStr)
        for node in ast.walk(tree):
            assert not isinstance(node, forbidden)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
                assert not (isinstance(node.left, ast.Constant) and isinstance(node.left.value, str))
            if not isinstance(node, ast.Call):
                continue
            if isinstance(node.func, ast.Name):
                assert node.func.id not in {"input", "open", "format"}
                if node.func.id == "print":
                    assert len(node.args) == 1 and not node.keywords
            if isinstance(node.func, ast.Attribute):
                assert node.func.attr not in {"format", "format_map", "read_text", "write_text"}

    return check
