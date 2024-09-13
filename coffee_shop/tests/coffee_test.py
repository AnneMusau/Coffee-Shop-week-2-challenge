import pytest
from coffee_shop.coffee import Coffee

def test_create_coffee():
    coffee = Coffee("Americano")
    assert coffee.name == "Americano"

def test_create_coffee_name_too_short():
    with pytest.raises(ValueError):
        Coffee("Esp")  # Coffee name should be at least 3 characters long

def test_change_coffee_name():
    coffee = Coffee("Latte")
    with pytest.raises(AttributeError):
        coffee.name = "Mocha"  # Coffee name cannot be changed after initialization
