import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
	city = ""

	if request.method == "POST":
		city = request.form["city"]

	print(city)
	APPID = ""	# insert your APPID
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID={}"
	req = requests.get(url.format(city, APPID)).json()

	weather_data = None

	if req["cod"] == 200:
		weather_data = {
			"city": req["name"],
			"icon": req["weather"][0]["icon"],
			"description": req["weather"][0]["description"],
			"temperature": req["main"]["temp"]
		}

	return render_template("index.html", title="Weather App", weather_data=weather_data)