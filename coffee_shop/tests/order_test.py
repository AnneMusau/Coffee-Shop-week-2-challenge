import pytest
from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee
from coffee_shop.order import Order

def test_order_initialization():
    customer = Customer("George")
    coffee = Coffee("Americano")
    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5

def test_order_price_validation():
    customer = Customer("Harry")
    coffee = Coffee("Macchiato")

    # Valid price
    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)

    # Invalid price: not a number
    with pytest.raises(TypeError):
        Order(customer, coffee, "free")

def test_order_immutable_price():
    customer = Customer("Ivy")
    coffee = Coffee("Mocha")
    order = Order(customer, coffee, 4.5)
    
    # Attempt to modify the price should raise an exception
    with pytest.raises(AttributeError):
        order.price = 5.0
