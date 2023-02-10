import requests
from dotenv import load_dotenv
import os

#Getting the API key from the .env file, and save it into the variable. This is for saftey reasons
load_dotenv()
apiKey = os.getenv("API_KEY")


#Getting the latutide and longitude based on location
def getLatLon(cityName, stateCode, countryCode, APIKey):
    #Calling API, and saving it into a valid JSON object
    ApiResponse = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={cityName},{stateCode},{countryCode}&appid={APIKey}'
    ).json()

    locationData = ApiResponse[0]
    Lat = locationData.get('lat')
    Lon = locationData.get('lon')
    
    return Lat, Lon

#returns the current weather conditions for the lon and lat
def getWeatherConditions(lat, lon, ApiKey):
    ApiResponse = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ApiKey}'
    ).json()



if __name__ == "__main__":
    lat, lon = getLatLon("Toronto", "ON", "Canada", apiKey)
    getWeatherConditions(lat, lon, apiKey)