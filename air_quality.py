import geocoder
g = geocoder.ip('me')

latitude = g.latlng[0]
longitude = g.latlng[1]
