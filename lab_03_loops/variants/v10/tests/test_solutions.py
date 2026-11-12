"""Проверки ЛР №3, вариант №10."""

import math
from math import cos, sin

import pytest

LEGACY = False
MODE = 'sum'
SIGN = '>'
RESULT_LABEL = 'Сумма'
GRID = (
    -4.0,
    -3.5,
    -3.0,
    -2.5,
    -2.0,
    -1.5,
    -1.0,
    -0.5,
    0.0,
    0.5,
    1.0,
    1.5,
    2.0,
    2.5,
    3.0,
    3.5,
    4.0,
)


def reference_y(x):
    if x < 0:
        y = x ** 2 - 1
    elif 0 < x < 1.5:
        y = cos(x)
    elif x > 1.5:
        y = sin(x - 1)
    else:
        y = None
    return y

def parse_table(text):
    result = []
    for line in text.splitlines():
        if "|" not in line:
            continue
        left, right = map(str.strip, line.split("|", 1))
        try:
            x = float(left)
        except ValueError:
            continue
        result.append((x, None if right == "не определено" else float(right)))
    return result


def parse_total(text):
    line = next(line for line in text.splitlines() if line.startswith(RESULT_LABEL))
    value = line.rsplit(" = ", 1)[1]
    return None if value == "None" else float(value)


def assert_table(text, grid, *, legacy=False):
    actual = parse_table(text)
    assert len(actual) == len(grid)
    expected_values = []
    for (got_x, got_y), x in zip(actual, grid):
        assert got_x == pytest.approx(x, abs=5e-8)
        expected = reference_y(x)
        if legacy and x == 0:
            expected = 1.0
        if legacy and x == 1.5:
            expected = math.sin(0.5)
        if expected is None:
            assert got_y is None
        else:
            assert got_y == pytest.approx(expected, rel=1e-9, abs=5e-7 if legacy else 1e-9)
            expected_values.append(expected)
    selected = [y for y in expected_values if not SIGN or (y > 0 if SIGN == ">" else y < 0)]
    if MODE == "sum":
        expected_total = math.fsum(selected)
    elif MODE == "prod":
        expected_total = math.prod(selected)
    elif MODE == "max":
        expected_total = max(selected, default=None)
    else:
        expected_total = min(selected, default=None)
    actual_total = parse_total(text)
    if expected_total is None:
        assert actual_total is None
    else:
        assert actual_total == pytest.approx(expected_total, abs=5e-7, rel=1e-9)


@pytest.mark.parametrize("level", ("noob", "basic", "advanced"))
def test_every_grid_point_and_total(level, run_solution, tmp_path):
    legacy = LEGACY and level != "noob"
    result = run_solution(level, inputs=(-5, 5, 0.4) if legacy else None)
    assert result.returncode == 0, result.stderr
    assert_table(result.stdout, GRID, legacy=legacy)
    if level == "noob":
        assert not list(tmp_path.glob("*.txt"))
    elif legacy:
        path = tmp_path / "results" / "result_lab_3_v14.txt"
        text = path.read_text(encoding="utf-8")
        assert parse_table(text) == parse_table(result.stdout)
        assert parse_total(text) == parse_total(result.stdout)
    else:
        assert (tmp_path / "result.txt").read_text(encoding="utf-8") == result.stdout

def test_advanced_keeps_nondivisible_grid_inside_interval(run_solution, tmp_path):
    result = run_solution(
        "advanced", args=("--start", "0", "--end", "1", "--step", "0.6", "--output", "grid.txt"),
    )
    assert result.returncode == 0, result.stderr
    assert_table(result.stdout, (0.0, 0.6))
    assert (tmp_path / "grid.txt").read_text(encoding="utf-8") == result.stdout
    assert not (tmp_path / "result.txt").exists()


@pytest.mark.parametrize(("start", "end", "step"), (("0", "1", "0"), ("0", "1", "-1"), ("2", "1", "0.5"), ("0", "1", "nan")))
def test_advanced_rejects_invalid_interval(start, end, step, run_solution, tmp_path):
    result = run_solution(
        "advanced", args=("--start", start, "--end", end, "--step", step),
    )
    assert result.returncode != 0
    assert "Ошибка:" in result.stderr
    assert not (tmp_path / "result.txt").exists()

def test_noob_source_is_console_only(assert_noob_source):
    assert_noob_source()
