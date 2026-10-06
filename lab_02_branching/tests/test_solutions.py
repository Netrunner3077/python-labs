"""Тесты для ЛР №2, вариант 14."""
import math
import sys
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from advanced import compute_b


class TestBranch1:
    """0 < x < 1 и 0 < y < 1."""

    def test_typical(self):
        result = compute_b(x=0.5, y=0.7, a=1.0, c=2.0, d=1.0)
        expected = 2 * math.log(0.5) * max(0.5, math.sin(1), math.cos(1))
        assert result == pytest.approx(expected, rel=1e-9)

    def test_negative_result(self):
        assert compute_b(0.5, 0.7, 1.0, 2.0, 1.0) < 0


class TestBranch2:
    """x < 0 и y < 0."""

    def test_typical(self):
        assert compute_b(-1.0, -2.0, 1.0, 1.0, 1.0) == -2.0


class TestBranch3:
    """В противном случае."""

    def test_x_positive_y_positive(self):
        assert compute_b(2.0, 3.0, 5.0, 1.0, 1.0) == 7.0

    def test_x_positive_y_negative(self):
        assert compute_b(0.5, -1.0, 4.0, 1.0, 1.0) == 4.5
