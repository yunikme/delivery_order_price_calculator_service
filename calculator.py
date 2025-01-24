from haversine import haversine, Unit   

def calculate_distance(coordinate_user, coordinate_venue):
    return int(haversine(coordinate_venue, coordinate_user, unit=Unit.METERS))

def calculate_delivery_fee(base_price, coef_a, coef_b, distance):
    del_fee = int(base_price + coef_a + (coef_b * distance)/10)
    return del_fee

def calculate_total_price(small_order_surcharge, cart_value, delivery_fee):
    return small_order_surcharge + cart_value + delivery_fee