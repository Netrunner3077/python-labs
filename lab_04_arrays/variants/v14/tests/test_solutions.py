"""Проверки ЛР №4, вариант №14."""

import ast
import random
import re

import pytest

ROWS = 10
COLUMNS = 9
LOW = -50
HIGH = 20
LEGACY_SIX = False
LEVELS = ('noob',)
CASES = (
    ([
        -50, 20, 0, -30, -20, -11, -10, -5, -1,
        1, 5, 10, 15, 19, 20, -50, 20, 0,
        -30, -20, -11, -10, -5, -1, 1, 5, 10,
        15, 19, 20, -50, 20, 0, -30, -20, -11,
        -10, -5, -1, 1, 5, 10, 15, 19, 20,
        -50, 20, 0, -30, -20, -11, -10, -5, -1,
        1, 5, 10, 15, 19, 20, -50, 20, 0,
        -30, -20, -11, -10, -5, -1, 1, 5, 10,
        15, 19, 20, -50, 20, 0, -30, -20, -11,
        -10, -5, -1, 1, 5, 10, 15, 19, 20,
    ], [2, 10, 11, 12, 13, 14, 15, 17, 25, 26, 27, 28, 29, 30, 32, 40, 41, 42, 43, 44, 45, 47, 55, 56, 57, 58, 59, 60, 62, 70, 71, 72, 73, 74, 75, 77, 85, 86, 87, 88, 89, 90]),
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
    ], []),
)


def reference(matrix):
    a = [value for row in matrix for value in row]
    def keep(x: int, i: int, j: int) -> bool:
        return x > 0

    transformed = [
        [x if keep(x, i, j) else 0 for j, x in enumerate(row)]
        for i, row in enumerate(matrix)
    ]
    selected = [
        (i * len(row) + j + 1, x)
        for i, row in enumerate(matrix)
        for j, x in enumerate(row)
        if keep(x, i, j)
    ]
    values = [x for _, x in selected]
    result = [i for i, _ in selected]
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

def read_legacy_matrix(text, rows):
    lines = text.split("Исходная матрица:", 1)[1].lstrip("\n").splitlines()
    return [list(map(int, line.split())) for line in lines[:rows]]


def read_positions(text):
    return [
        tuple(map(int, groups))
        for groups in re.findall(r"B\[(\d+)\] \(номер (\d+)\) = (\d+)", text)
    ]


@pytest.mark.parametrize("level", ("basic", "advanced"))
def test_legacy_positions_and_result_file(level, run_solution, tmp_path):
    result = run_solution(level, inputs=("",) * 5 if level == "advanced" else None)
    assert result.returncode == 0, result.stderr
    matrix = read_legacy_matrix(result.stdout, ROWS)
    assert [len(row) for row in matrix] == [COLUMNS] * ROWS
    data = [x for row in matrix for x in row]
    assert all(LOW <= x <= HIGH for x in data)
    expected = [(i, i + 1, x) for i, x in enumerate(data) if x > 0]
    assert read_positions(result.stdout) == expected
    if level == "basic":
        generator = random.Random(14)
        assert data == [generator.randint(LOW, HIGH) for _ in range(ROWS * COLUMNS)]
    else:
        saved = (tmp_path / "result_lab_4_v14.txt").read_text(encoding="utf-8")
        assert read_legacy_matrix(saved, ROWS) == matrix
        assert read_positions(saved) == expected


def test_advanced_all_nonpositive(run_solution):
    result = run_solution("advanced", inputs=(4, -1, 0, 2, 2))
    assert result.returncode == 0, result.stderr
    matrix = read_legacy_matrix(result.stdout, 2)
    assert [len(row) for row in matrix] == [2, 2]
    assert all(-1 <= x <= 0 for row in matrix for x in row)
    assert read_positions(result.stdout) == []
    assert "Положительных элементов нет" in result.stdout


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="ЛР №4 v14: main не повторяет ввод при k != n*m")
def test_advanced_retries_inconsistent_dimensions(run_solution):
    result = run_solution("advanced", inputs=(5, -50, 20, 2, 2, 4, -50, 20, 2, 2))
    assert result.returncode == 0, result.stderr
    assert len(read_legacy_matrix(result.stdout, 2)) == 2


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="ЛР №4 v14: нулевые размеры принимаются")
def test_advanced_rejects_zero_dimensions(run_solution):
    result = run_solution("advanced", inputs=(0, -50, 20, 0, 9))
    assert "Исходная матрица:" not in result.stdout

def test_noob_source_is_console_only(assert_noob_source):
    assert_noob_source()
