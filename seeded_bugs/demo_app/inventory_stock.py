"""Stock-reservation helpers."""

import threading

_inventory: dict[str, int] = {}
_lock = threading.Lock()


def add_stock(item_id, quantity):
    with _lock:
        _inventory[item_id] = _inventory.get(item_id, 0) + quantity


def reserve_stock(item_id, quantity):
    """Reserve `quantity` units of `item_id`, if available."""
    with _lock:
        current = _inventory.get(item_id, 0)
        if current >= quantity:
            _inventory[item_id] = current - quantity
            return True
        return False
