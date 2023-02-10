# My Weather App

import requests

def getLatLon(cityName, stateCode, countryCode, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={cityName}
                            ,{stateCode},{countryCode}&appid={API_key}')

