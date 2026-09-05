from types import SimpleNamespace

from seeded_bugs.demo_app.inventory import recent_items


def make_cart(items):
    return SimpleNamespace(items=items)


def test_recent_items_returns_exactly_n_items():
    cart = make_cart(["a", "b", "c", "d", "e"])
    result = recent_items(cart, 3)
    assert len(result) == 3
    # Most recent first
    assert result == ["e", "d", "c"]


def test_recent_items_unpacking_matches_n():
    cart = make_cart(["a", "b", "c", "d"])
    x, y, z = recent_items(cart, 3)
    assert (x, y, z) == ("d", "c", "b")


def test_recent_items_zero():
    cart = make_cart(["a", "b", "c"])
    assert recent_items(cart, 0) == []


def test_recent_items_more_than_available():
    cart = make_cart(["a", "b"])
    result = recent_items(cart, 5)
    assert result == ["b", "a"]
