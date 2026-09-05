"""Tiny demo shopping-cart module."""


class Cart:
    def __init__(self):
        self.items = []


def add_item(cart, item):
    return cart.items.append(item)


def total_price(cart):
    return sum(item.price for item in cart.items)
