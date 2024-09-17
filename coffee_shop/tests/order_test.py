import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_price_validation():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)
    
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)
