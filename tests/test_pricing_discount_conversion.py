import pytest

from seeded_bugs.demo_app.pricing import apply_discount


def test_apply_discount_with_percent_string_and_float_price():
    # Reproduces TypeError: can't multiply sequence by non-int of type 'float'
    result = apply_discount(100.0, "15%")
    assert result == pytest.approx(85.0)


def test_apply_discount_with_percent_string_and_int_price():
    result = apply_discount(200, "10%")
    assert result == pytest.approx(180.0)


def test_apply_discount_with_numeric_discount():
    result = apply_discount(50.0, 20)
    assert result == pytest.approx(40.0)
