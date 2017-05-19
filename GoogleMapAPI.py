import requests

API_KEY  = "xxxxxxxxxxxxxxxxxxxxxxxx"


def get_loc(address, state):
	
	base_url = "https://maps.googleapis.com/maps/api/geocode/json?"
	params = {
		"key":get_loc.API_KEY,
		"address":address+' , '+state}

	conn = requests.get(base_url, params=params)
	info = conn.json()

	try:
		loc = info['results'][0]['geometry']['location']
		latitude, longitude = loc['lat'], loc['lng']
	except:
		return None, None
	return latitude, longitude

get_loc.API_KEY = API_KEY
