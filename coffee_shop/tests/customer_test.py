import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_customer_initialization():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_orders():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order1 = Order(customer, coffee, 5.0)
    order2 = Order(customer, coffee, 6.0)
    
    assert customer.orders() == [order1, order2]

def test_customer_coffees():
    customer = Customer("Alice")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")
    order1 = Order(customer, coffee1, 5.0)
    order2 = Order(customer, coffee2, 6.0)
    
    assert set(customer.coffees()) == {coffee1, coffee2}
