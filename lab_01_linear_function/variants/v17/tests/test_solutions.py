"""Проверки ЛР №1, вариант №17."""

import pytest

CASES = (
    (1.385, -1.2, 0.3352, 0),
    (1.4127, -1.176, 0.3308, 0),
)

def number(line):
    return float(line.rsplit(" = ", 1)[1])


@pytest.mark.parametrize("level", ("noob", "basic", "advanced"))
@pytest.mark.parametrize(("x", "y", "rounded", "integer"), CASES, ids=("control", "alternate"))
def test_value_and_integer_part(level, x, y, rounded, integer, run_solution, tmp_path):
    if level == "noob":
        result = run_solution(level, assignments={"x": x, "y": y})
    else:
        result = run_solution(level, files={"input.txt": f"{x} {y}\n"})
    assert result.returncode == 0, result.stderr
    value_line, integer_line = result.stdout.splitlines()
    assert number(value_line) == pytest.approx(rounded, abs=1e-12)
    assert int(integer_line.rsplit(" = ", 1)[1]) == integer
    if level == "noob":
        assert not list(tmp_path.glob("*.txt"))
    else:
        assert (tmp_path / "result.txt").read_text(encoding="utf-8") == result.stdout


@pytest.mark.parametrize("level", ("basic", "advanced"))
def test_file_accepts_decimal_comma(level, run_solution):
    x, y, expected, _ = CASES[0]
    source = f"{x}\n{y}\n".replace(".", ",")
    result = run_solution(level, files={"input.txt": source})
    assert result.returncode == 0, result.stderr
    assert number(result.stdout.splitlines()[0]) == pytest.approx(expected)


def test_advanced_supports_custom_paths(run_solution, tmp_path):
    x, y, _, _ = CASES[0]
    result = run_solution(
        "advanced", args=("--input", "values.txt", "--output", "answer.txt"),
        files={"values.txt": f"{x}\n{y}\n"},
    )
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "answer.txt").read_text(encoding="utf-8") == result.stdout
    assert not (tmp_path / "result.txt").exists()


@pytest.mark.parametrize("source", (None, "text\n", "1\n", "1 2 3\n"))
def test_advanced_reports_invalid_or_missing_input(source, run_solution, tmp_path):
    files = None if source is None else {"input.txt": source}
    result = run_solution("advanced", files=files)
    assert result.returncode != 0
    assert "Ошибка:" in result.stderr
    assert not (tmp_path / "result.txt").exists()


def test_noob_starts_with_assigned_control_values(run_solution, tmp_path):
    result = run_solution("noob")
    assert result.returncode == 0, result.stderr
    assert number(result.stdout.splitlines()[0]) == pytest.approx(CASES[0][2])
    assert not list(tmp_path.glob("*.txt"))

def test_noob_source_is_console_only(assert_noob_source):
    assert_noob_source()
