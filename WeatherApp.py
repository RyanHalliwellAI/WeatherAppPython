import requests
from dotenv import load_dotenv
import os

#Getting the API key from the .env file, and save it into the variable. This is for saftey reasons
load_dotenv()
apiKey = os.getenv("API_KEY")



def getLatLon(cityName, stateCode, countryCode, APIKey):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={cityName}
                            ,{stateCode},{countryCode}&appid={APIKey}')
    
    print(response)

getLatLon("Toronto", "ON", "Canada", apiKey)