import pprint
import requests
# from dateutil.parser import parse

class YahooWeatherForecast:

	def __init__(self):
		self._city_cache = {}

	def get(self, city):
		if city in self._city_cache:
			return self._city_cache(city)
		url = f"https://query.yahooapis.com/v1/public/yql?q="
		+ f"select%20*%20from%20weather.forecast%20where%20w"
		+ f"oeid%20in%20(select%20woeid%20from%20geo.places("
		+ f"1)%20where%20text%3D%22{city}%22)%20and%20u%3D%2"
		+ f"7c%27&format=json&env=store%3A%2F%2Fdatatables.o"
		+ f"rg%2Falltableswithkey"
		print("sending HTTP request")
		data = requests.get(url).json()
		forecast_data = data["query"]["results"]["channel"]["item"]["forecast"]
		forecast = []
		for day_data in forecast_data:
			forecast.append({
				"data": day_data["date"],
				"high_temp": day_data["high"]
			})
		self._city_cache[city] = forecast
		return forecast



class CityInfo:

	def __init__(self, city, weather_forecast=None):
		self.city = city
		self._weather_forecast = weather_forecast or YahooWeatherForecast()

	def weather_forecast(self):
		return self._weather_forecast.get(self.city)


	
def _main():
	weather_forecast = YahooWeatherForecast()
	for i in range(5):								# 5 запросов
		city_info = CityInfo("Moscow", weather_forecast=weather_forecast)
		forecast = city_info.weather_forecast()
	pprint.pprint(forecast)



if __name__ == "__main__":
	_main()