from flask import Flask, render_template, request
from WeatherApp import main as getWeather

#intilzing the website using flask.
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def index():
    weatherData = None
    if request.method == 'POST':
        #print("Test")
        city =  request.form['cityName']
        state =  request.form['stateName']
        country =  request.form['countryName']
        weatherData = (getWeather(city, state, country))
        
    return render_template("index.html", weatherData = weatherData)

if __name__ == "__main__":
    app.run(debug=True)