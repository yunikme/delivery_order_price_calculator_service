import requests

def get_query_parameter(arguments):
    venue_slug = arguments.get('venue_slug')
    cart_value = arguments.get('cart_value', type=int)
    user_lat = arguments.get('user_lat', type=float) 
    user_lon = arguments.get('user_lon', type=float)    
    return venue_slug, cart_value, user_lat, user_lon 

def request_get(url):
    response_url = requests.get(url)
    if response_url.status_code == 200:
        json_data = response_url.json()
        return json_data 
    raise ValueError("Failed to retried data")
  
def validate_coordinate(lat, lon):
    if not isinstance(lat, (int, float)):
        raise ValueError("latitude must be a number")
    if not isinstance(lon, (int, float)):
        raise ValueError("longitude must be a number")
    return   

def validate_request_data(venue_slug, cart_value, user_lat, user_lon):
    if venue_slug == None or cart_value== None or user_lat == None or user_lon == None:
        raise ValueError("Please provide venue_slug, cart_value, user_lat,and user_lon.")
    if cart_value <= 0 or not isinstance(cart_value, (int, float)):
        raise ValueError("Please provide cart_value > 0")
    if validate_coordinate(user_lat, user_lon):
        raise ValueError("coordinates must be number")
    return