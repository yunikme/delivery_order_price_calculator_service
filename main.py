from calculator import *
from request_parameter import *
from flask import Flask, request, jsonify
import config 
import requests

dopc = Flask(__name__)
@dopc.route('/api/v1/delivery-order-price', methods=['GET'])
def calculator_service():
    try:
        venue_slug, cart_value, user_lat, user_lon = get_query_parameter(request.args)
        validate_request_data(venue_slug, cart_value, user_lat, user_lon)
  
    except ValueError as e: 
        return jsonify({"error": f"{e}"}), 400 
    
    coordinate_user  = (user_lat, user_lon)

    try:
        static_response = request_get(config.get_home_assignment_static_url(venue_slug))    
    except ValueError:
        return jsonify({"error":"Failed to retried data"}), 400
    
    coordinates = static_response.get("venue_raw", {}).get("location",{}).get("coordinates")

    try:
        validate_coordinate(coordinates[1], coordinates[0])
    except ValueError:
        return jsonify({"error": f"{e}"}), 400 
    coordinate_venue = (coordinates[1],coordinates[0])#(al,lon) #refaktor jadi 2 variabel
    distance = calculate_distance(coordinate_user, coordinate_venue) 
    
    try:
        dynamic_response = request_get(config.get_home_assignment_dynamic_url(venue_slug))    
    except ValueError:
        return jsonify({"error":"Failed to retried data"}), 400   
    
    delivery_specs =  dynamic_response.get("venue_raw", {}).get("delivery_specs", {})
    distance_ranges = delivery_specs.get("delivery_pricing", {}).get("distance_ranges",{})
    base_price = delivery_specs.get("delivery_pricing", {}).get ("base_price", 0) 
    order_minimum_no_surcharge = delivery_specs.get("order_minimum_no_surcharge", 0)    
    

    for range_distance in distance_ranges:
        if range_distance["max"]==0:
            return jsonify({"error":"delivery would not be possible"}), 400
        elif range_distance ["min"] <= distance < range_distance["max"]:
            a = range_distance["a"]
            b = range_distance["b"]
            break        
    
    small_order_surcharge = max(0, order_minimum_no_surcharge - cart_value)
    delivery_fee = calculate_delivery_fee(base_price, a,b, distance)
    total_price = calculate_total_price(small_order_surcharge, cart_value, delivery_fee) 
    
    return jsonify(
        {
            "total_price": total_price,
            "small_order_surcharge": small_order_surcharge,
            "cart_value": cart_value,
            "delivery": {
                "fee": delivery_fee,
                "distance": distance
            }
        }
    ), 200

if __name__ == '__main__':
    dopc.run(debug=True, port=8000)