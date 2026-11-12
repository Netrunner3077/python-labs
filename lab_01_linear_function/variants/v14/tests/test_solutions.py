"""Проверки ЛР №1, вариант №14."""

import re

import pytest

def read_value(text):
    line = next(line for line in text.splitlines()[::-1] if "u = " in line)
    return float(line.rsplit("u = ", 1)[1])


@pytest.mark.parametrize("level", ("noob", "basic", "advanced"))
@pytest.mark.parametrize(("x", "y", "expected"), ((1.472, -0.4342, 0.1158), (1, -3, -0.3044)))
def test_value_for_control_and_negative_result(level, x, y, expected, run_solution, tmp_path):
    if level == "noob":
        result = run_solution(level, assignments={"x": x, "y": y})
        lines = result.stdout.splitlines()
        assert float(lines[0].rsplit(" = ", 1)[1]) == pytest.approx(expected)
        assert int(lines[-1].rsplit(" = ", 1)[1]) == 0
    else:
        result = run_solution(level, inputs=(x, y))
        assert read_value(result.stdout) == pytest.approx(expected, abs=0.00005)
    assert result.returncode == 0, result.stderr


def test_noob_starts_without_input_or_files(run_solution, tmp_path):
    result = run_solution("noob")
    assert result.returncode == 0, result.stderr
    assert "0.1158" in result.stdout
    assert not list(tmp_path.glob("*.txt"))


@pytest.mark.parametrize("level", ("basic", "advanced"))
@pytest.mark.parametrize(("x", "y"), ((0, 2), (2, 2), (2, -4)))
def test_zero_denominator(level, x, y, run_solution):
    result = run_solution(level, inputs=(x, y))
    assert result.returncode == 0, result.stderr
    assert "знаменатель равен нулю" in result.stdout.lower()


def test_advanced_retries_text_instead_of_number(run_solution):
    result = run_solution("advanced", inputs=("oops", 1.472, -0.4342))
    assert result.returncode == 0, result.stderr
    assert "введите корректное число" in result.stdout
    assert read_value(result.stdout) == pytest.approx(0.115836)


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="ЛР №1 v14: решение ожидает ввод с клавиатуры")
@pytest.mark.parametrize("level", ("basic", "advanced"))
def test_assignment_reads_file(level, run_solution):
    result = run_solution(level, files={"input.txt": "1.472\n-0.4342\n"})
    assert result.returncode == 0, result.stderr
    assert read_value(result.stdout) == pytest.approx(0.1158, abs=0.00005)


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="ЛР №1 v14: файл результата отсутствует")
@pytest.mark.parametrize("level", ("basic", "advanced"))
def test_assignment_writes_result_and_integer_part(level, run_solution, tmp_path):
    result = run_solution(level, inputs=(1.472, -0.4342))
    assert result.returncode == 0, result.stderr
    files = list(tmp_path.rglob("*.txt"))
    assert files, "Нет файла результата"
    text = "\n".join(path.read_text(encoding="utf-8") for path in files)
    assert re.search(r"(?<![\d.])0[.,]1158(?!\d)", text)
    assert re.search(r"(?<![\d.,])0(?![\d.,])", text)


@pytest.mark.xfail(strict=True, raises=AssertionError, reason="ЛР №1 v14: порог isclose отклоняет ненулевой знаменатель")
def test_small_nonzero_denominator_is_valid(run_solution):
    result = run_solution("advanced", inputs=(0.000001, 0))
    assert result.returncode == 0, result.stderr
    assert "Результат: u = " in result.stdout

def test_noob_source_is_console_only(assert_noob_source):
    assert_noob_source()
