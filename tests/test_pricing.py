from seeded_bugs.demo_app.pricing import apply_discount


def test_apply_discount_accepts_percent_string():
    result = apply_discount(200.0, "25%")

    assert result == 150.0
