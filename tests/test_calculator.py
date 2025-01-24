import pytest
from calculator import calculator_distance, calculator_delivery_fee, calculator_total_price

def test_calculate_distance():
    user_coordinates = (60.1699, 24.9384)
    venue_coordinates = (60.1700, 24.9400)
    distance = calculate_distance(user_coordinates, venue_coordinates)
    assert distance > 0 

def test_calculate_delivery_fee():
    base_price = 100
    a = 10
    b = 5
    distance = 2000
    fee = calculate_delivery_fee(base_price, a, b, distance)
    assert fee == 1100 

def test_calculate_total_price():
    surcharge = 10
    cart_value = 50
    delivery_fee = 20
    total_price = calculate_total_price(surcharge, cart_value, delivery_fee)
    assert total_price == 80    