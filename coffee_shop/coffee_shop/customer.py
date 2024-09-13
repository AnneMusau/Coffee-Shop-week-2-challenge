# customer.py

from order import Order

class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("_define-ocg_ Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.orders().append(order)

    @classmethod
    def most_aficionado(cls, coffee):
        customers_spending = {customer: sum(order.price for order in customer.orders() if order.coffee == coffee) for customer in coffee.customers()}
        return max(customers_spending, key=customers_spending.get) if customers_spending else None
