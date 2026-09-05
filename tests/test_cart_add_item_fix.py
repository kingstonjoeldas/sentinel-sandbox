import pytest
from seeded_bugs.demo_app.cart import Cart, add_item


def test_add_item_returns_cart_not_none():
    cart = Cart()
    result = add_item(cart, "widget")
    assert result is not None
    assert result is cart
    assert result.items == ["widget"]


def test_chained_add_item_reassignment_does_not_break():
    cart = Cart()
    cart = add_item(cart, "item1")
    cart = add_item(cart, "item2")
    assert cart is not None
    assert cart.items == ["item1", "item2"]
