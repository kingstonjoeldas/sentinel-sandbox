from seeded_bugs.demo_app.cart import Cart, add_item
from seeded_bugs.demo_app.inventory import recent_items


def test_recent_items_returns_exactly_n():
    cart = Cart()
    for label in ["a", "b", "c", "d"]:
        add_item(cart, label)

    result = recent_items(cart, 3)

    assert len(result) == 3
    assert result == ["d", "c", "b"]
