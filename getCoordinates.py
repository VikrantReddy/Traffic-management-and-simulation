import urllib.request, urllib.parse, urllib.error
import json
import ssl
import os

API_KEY = os.environ.get("API_KEY",False)

# If you dont have a Google Places API key, find it here
# https://developers.google.com/maps/documentation/geocoding/intro

if API_KEY is False:
    API_KEY = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

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

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    data = urllib.request.urlopen(url, context=ctx)
    decodeddata = data.read().decode()

    return decodeddata


def getCordinates(data):
    try:
        js = json.loads(data)
    except TypeError:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        return -1

    latitude = js['results'][0]['geometry']['location']['lat']
    longitude = js['results'][0]['geometry']['location']['lng']

    location = js['results'][0]['formatted_address']
    
    return latitude,longitude,location

    
if __name__ == "__main__" : 
    while True:
        address = input('Enter location: ')
        data = getData(address=address)

        print('Retrieved', len(data), 'characters')

        latitude,longitude,location = getCordinates(data=data)

        print(f"latitude:{latitude}, longitude= {longitude}")
        print(f"Loc: {location}")

    
