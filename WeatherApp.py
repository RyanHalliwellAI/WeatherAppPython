import requests
from dotenv import load_dotenv
from dataclasses import dataclass
import os

#Getting the API key from the .env file, and save it into the variable. This is for saftey reasons
load_dotenv()
apiKey = os.getenv("API_KEY")

@dataclass
class Weather:
    
    main: str
    description: str
    icon: str
    temp: float


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
        f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ApiKey}&units=metric'
    ).json()
    
    WeatherData = Weather(
        main = ApiResponse.get('weather')[0].get('main'),
        description= ApiResponse.get('weather')[0].get('description'),
        icon = ApiResponse.get('weather')[0].get('icon'),
        temp = ApiResponse.get('main').get('temp')

    )
    return WeatherData
    #print(ApiResponse)

#Main method to send in the cityName, state and country name to get the weather.
def main(cityName, stateName, countryName):
    lat, lon = getLatLon(cityName, stateName, countryName, apiKey)
    weatherData = getWeatherConditions(lat, lon, apiKey)
    return weatherData

    

if __name__ == "__main__":
    lat, lon = getLatLon("Toronto", "ON", "Canada", apiKey)
    print(getWeatherConditions(lat, lon, apiKey))