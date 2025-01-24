HOME_ASSIGNMENT_BASE_URL = "https://consumer-api.development.dev.woltapi.com/home-assignment-api/v1/venues"

def get_home_assignment_static_url(venue_slug):
    return f"{HOME_ASSIGNMENT_BASE_URL}/{venue_slug}/static"

def get_home_assignment_dynamic_url(venue_slug):
    return f"{HOME_ASSIGNMENT_BASE_URL}/{venue_slug}/dynamic"
