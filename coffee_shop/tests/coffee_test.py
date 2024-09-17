import pytest
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order
from coffee_shop.customer import Customer

def test_coffee_initialization():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Esp")

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order1 = Order(customer, coffee, 4.5)
    order2 = Order(customer, coffee, 5.0)
    
    assert coffee.orders() == [order1, order2]

def test_coffee_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("Bob")
    customer2 = Customer("Alice")
    order1 = Order(customer1, coffee, 4.5)
    order2 = Order(customer2, coffee, 5.0)
    
    assert set(coffee.customers()) == {customer1, customer2}
