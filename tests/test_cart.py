from seeded_bugs.demo_app.cart import Cart, add_item


def test_add_item_returns_the_cart():
    cart = Cart()
    result = add_item(cart, "widget")
    assert result is cart
    assert result.items == ["widget"]
