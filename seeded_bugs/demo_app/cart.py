"""Tiny demo shopping-cart module."""


class Cart:
    def __init__(self):
        self.items = []


def add_item(cart, item):
    cart.items.append(item)
    return cart


def total_price(cart):
    return sum(item.price for item in cart.items)
