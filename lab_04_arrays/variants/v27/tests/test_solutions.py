"""Проверки ЛР №4, вариант №27."""

import ast
import random

import pytest

ROWS = 11
COLUMNS = 9
LOW = -20
HIGH = 70
LEGACY_SIX = False
LEVELS = ('noob', 'basic', 'advanced')
CASES = (
    ([
        -20, 70, 0, -20, -11, -10, -5, -1, 1,
        5, 10, 15, 19, 20, 29, 30, 31, -20,
        70, 0, -20, -11, -10, -5, -1, 1, 5,
        10, 15, 19, 20, 29, 30, 31, -20, 70,
        0, -20, -11, -10, -5, -1, 1, 5, 10,
        15, 19, 20, 29, 30, 31, -20, 70, 0,
        -20, -11, -10, -5, -1, 1, 5, 10, 15,
        19, 20, 29, 30, 31, -20, 70, 0, -20,
        -11, -10, -5, -1, 1, 5, 10, 15, 19,
        20, 29, 30, 31, -20, 70, 0, -20, -11,
        -10, -5, -1, 1, 5, 10, 15, 19, 20,
    ], 10),
    ([
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0,
    ], 0),
)


def reference(matrix):
    a = [value for row in matrix for value in row]
    values = [max(row) for row in matrix]
    transformed = [[x] for x in values]
    result = min(values)
    return transformed, result

def read_matrices(text):
    original, transformed = text.split("Преобразованная матрица:\n", 1)
    matrix = [list(map(int, row.split())) for row in original.splitlines()[1:]]
    lines = transformed.splitlines()
    if LEGACY_SIX:
        count = int(lines[-2].rsplit(" = ", 1)[1])
        total = int(lines[-1].rsplit(" = ", 1)[1])
        return matrix, [list(map(int, row.split())) for row in lines[:-2]], [count, total]
    summary = ast.literal_eval(lines[-1].rsplit(" = ", 1)[1])
    return matrix, [list(map(int, row.split())) for row in lines[:-1]], summary


def same_number(actual, expected):
    if isinstance(expected, float):
        assert actual == pytest.approx(expected)
    else:
        assert actual == expected


@pytest.mark.parametrize("level", LEVELS)
def test_matrix_and_result_recomputed_from_output(level, run_solution, tmp_path):
    result = run_solution(level)
    assert result.returncode == 0, result.stderr
    matrix, transformed, summary = read_matrices(result.stdout)
    assert [len(row) for row in matrix] == [COLUMNS] * ROWS
    assert all(LOW <= value <= HIGH for row in matrix for value in row)
    expected_matrix, expected_summary = reference(matrix)
    assert transformed == expected_matrix
    same_number(summary, expected_summary)
    if level == "noob":
        assert not list(tmp_path.glob("*.txt"))
    else:
        assert (tmp_path / "result.txt").read_text(encoding="utf-8") == result.stdout


@pytest.mark.parametrize("level", LEVELS)
@pytest.mark.parametrize(("values", "expected"), CASES, ids=("boundaries", "all-zero"))
def test_controlled_values_and_ties(level, values, expected, run_solution):
    if level == "noob":
        result = run_solution(level, assignments={"a": values})
    else:
        result = run_solution(level, fixed_values=values)
    assert result.returncode == 0, result.stderr
    matrix, transformed, summary = read_matrices(result.stdout)
    assert [x for row in matrix for x in row] == values
    assert transformed == reference(matrix)[0]
    same_number(summary, expected)

def test_advanced_seed_and_custom_output(run_solution, tmp_path):
    seed = 123
    result = run_solution("advanced", args=("--seed", str(seed), "--output", "matrix.txt"))
    assert result.returncode == 0, result.stderr
    matrix, transformed, summary = read_matrices(result.stdout)
    generator = random.Random(seed)
    assert [x for row in matrix for x in row] == [
        generator.randint(LOW, HIGH) for _ in range(ROWS * COLUMNS)
    ]
    expected_matrix, expected_summary = reference(matrix)
    assert transformed == expected_matrix
    same_number(summary, expected_summary)
    assert (tmp_path / "matrix.txt").read_text(encoding="utf-8") == result.stdout
    assert not (tmp_path / "result.txt").exists()

def test_noob_source_is_console_only(assert_noob_source):
    assert_noob_source()
