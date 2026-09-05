import pytest

from seeded_bugs.demo_app.pricing import apply_discount


def test_apply_discount_with_string_percent():
    # Should not raise TypeError and should compute correctly.
    result = apply_discount(200.0, "15%")
    assert result == pytest.approx(170.0)


def test_apply_discount_with_numeric_percent():
    result = apply_discount(200.0, 15)
    assert result == pytest.approx(170.0)
