from urllib import request, parse
import json
import ssl
import os

API_KEY = os.environ.get("API_KEY",False)

# If you dont have a Google Places API key, find it here
# https://developers.google.com/maps/documentation/geocoding/intro

if API_KEY is False:
    API_KEY = 42
    SERVICE_URL = 'http://py4e-data.dr-chuck.net/json?'
else :
    SERVICE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getData(address):
    if len(address) < 1:
        return

    parms = {}
    parms.update({'address' : address})

    if API_KEY is not False:
        parms['key'] = API_KEY

    url = SERVICE_URL + parse.urlencode(parms)

    print('Retrieving', url)
    raw_data = request.urlopen(url, context=ctx)
    decodeddata = raw_data.read().decode()

    return decodeddata


def getLocation(data):
    try:
        js_data = json.loads(data)
    except TypeError:
        js_data = None

    if not js_data or 'status' not in js_data or js_data['status'] != 'OK':
        return -1

    latitude = js_data['results'][0]['geometry']['location']['lat']
    longitude = js_data['results'][0]['geometry']['location']['lng']

    location = js_data['results'][0]['formatted_address']

    return latitude,longitude,location


if __name__ == "__main__" :
    while True:
        address = input('Enter location: ')
        decodeddata = getData(address=address)

        print('Retrieved', len(decodeddata), 'characters')

        latitude,longitude,location = getLocation(data=decodeddata)

        print(f"latitude:{latitude}, longitude= {longitude}")
        print(f"Loc: {location}")
