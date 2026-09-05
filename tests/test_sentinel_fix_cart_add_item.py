import pytest

from seeded_bugs.demo_app.cart import Cart, add_item, total_price


class Item:
    def __init__(self, price):
        self.price = price


def test_add_item_returns_cart_not_none():
    cart = Cart()
    result = add_item(cart, Item(10))
    assert result is not None
    assert result is cart
    assert result.items == [Item(10)].__len__() * [result.items[0]]  # placeholder to keep length check


def test_add_item_chained_usage_matches_reported_bug():
    cart = Cart()
    # Common caller pattern that triggered the AttributeError in production
    cart = add_item(cart, Item(5))
    cart = add_item(cart, Item(7))
    assert cart is not None
    assert total_price(cart) == 12
