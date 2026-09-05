"""Pricing helpers."""


def apply_discount(price, discount_percent):
    """Apply a percentage discount to a price.

    `discount_percent` may arrive as a string like "15%" (e.g. from a
    query param) and needs trimming and converting to a number first.
    """
    if isinstance(discount_percent, str):
        discount_percent = discount_percent.strip("%")
    discount_percent = float(discount_percent)
    return price - (price * discount_percent / 100)
