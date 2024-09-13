# Import the Order class from the order module
from coffee_shop.order import Order  # Make sure this import exists

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self.orders.append(order)
        return order
