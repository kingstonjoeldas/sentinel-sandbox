"""Order-history helpers."""


def recent_items(cart, n):
    """Return the n most recently added items, most recent first."""
    if n <= 0:
        return []
    return list(reversed(cart.items[-n:]))
