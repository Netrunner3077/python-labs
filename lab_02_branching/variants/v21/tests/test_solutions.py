"""Проверки ЛР №2, вариант №21."""

import re

import pytest

NAMES = ('x', 'b', 'c')
LEGACY = False
CASES = (
    ((6.0, 0.5, 2.0), 3.0),
    ((3.0, 0.5, -1.0), -2.520574461395797),
    ((2.0, 5.0, 2.0), 5.0),
    ((3.0, 0.5, 0.0), 0.5),
)
CASE_IDS = (
    'branch-1-case-1',
    'branch-2-case-2',
    'branch-3-case-3',
    'branch-3-case-4',
)

def values_from(text):
    return {
        key: float(value)
        for key, value in re.findall(
            r"(?:^|[\s,])([a-z]+)\s*=\s*([-+0-9.eE]+)", text
        )
    }


@pytest.mark.parametrize("level", ("noob", "basic", "advanced"))
@pytest.mark.parametrize(("inputs", "expected"), CASES, ids=CASE_IDS)
def test_branches_and_boundaries(level, inputs, expected, run_solution, tmp_path):
    assigned = dict(zip(NAMES, inputs))
    if level == "noob":
        result = run_solution(level, assignments=assigned)
    else:
        result = run_solution(level, inputs=inputs)
    assert result.returncode == 0, result.stderr
    last_line = result.stdout.splitlines()[-1]
    assert values_from(result.stdout) == {
        **assigned,
        **({"b": float(last_line.rsplit(" = ", 1)[1])} if LEGACY and level != "noob" else {}),
    }
    if expected is None:
        assert "не задана" in last_line
    else:
        tolerance = 5e-7 if LEGACY and level != "noob" else 1e-10
        assert float(last_line.rsplit(" = ", 1)[1]) == pytest.approx(
            expected, rel=1e-9, abs=tolerance
        )
    if level == "noob":
        assert not list(tmp_path.glob("*.txt"))
    else:
        report = (tmp_path / "result.txt").read_text(encoding="utf-8")
        if LEGACY:
            assert values_from(report) == values_from(result.stdout)
        else:
            assert result.stdout.endswith(report)
        expected_last = last_line.removeprefix("Результат: ") if LEGACY else last_line
        assert report.splitlines()[-1] == expected_last


def test_noob_default_case(run_solution, tmp_path):
    result = run_solution("noob")
    assert result.returncode == 0, result.stderr
    assert float(result.stdout.splitlines()[-1].rsplit(" = ", 1)[1]) == pytest.approx(CASES[0][1])
    assert not list(tmp_path.glob("*.txt"))


def test_advanced_retries_invalid_input(run_solution, tmp_path):
    inputs, expected = CASES[0]
    result = run_solution("advanced", inputs=("oops", *inputs))
    assert result.returncode == 0, result.stderr
    assert "веществен" in (result.stdout + result.stderr).lower()
    assert float(result.stdout.splitlines()[-1].rsplit(" = ", 1)[1]) == pytest.approx(
        expected, abs=5e-7
    )
    assert (tmp_path / "result.txt").is_file()

def test_noob_source_is_console_only(assert_noob_source):
    assert_noob_source()
