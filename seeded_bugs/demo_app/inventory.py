"""Order-history helpers."""


def recent_items(cart, n):
    """Return the n most recently added items, most recent first."""
    return list(reversed(cart.items[-n:]))
