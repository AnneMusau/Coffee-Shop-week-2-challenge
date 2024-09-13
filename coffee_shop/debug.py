from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

alice = Customer("Alice")
latte = Coffee("Latte")
order1 = Order(alice, latte, 5.0)

import ipdb; ipdb.set_trace()
