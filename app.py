from flask import Flask, render_template, request
from WeatherApp import main as getWeather

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)