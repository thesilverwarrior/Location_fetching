import geocoder

def get_location():
    g = geocoder.ip('me')
    return g.latlng  # Returns [latitude, longitude]

# Test
print(get_location())
