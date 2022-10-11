import meteostat
from meteostat import Point, Hourly
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

class WeatherObject():
    def __init__(self, temp, rhum, wdir, wspd, pres, prcp) -> None:
        self.temp = temp
        self.rhum = rhum
        self.wdir = wdir
        self.wspd = wspd
        self.pres = pres
        self.prcp = prcp

        self._rel = 0.0

def get_weather(location, time):
    data = Hourly(location, time-timedelta(1/24, 0), time)
    data = data.fetch()
    return WeatherObject(data.temp.iloc[0], data.rhum.iloc[0], data.wdir.iloc[0], data.wspd.iloc[0], data.pres.iloc[0], data.prcp.iloc[0])#, data["rhum"], data["wdir"], data["wspd"], data["pres"], data["prcp"])

def get_rel(weather):
    weather._rel = (4*weather.temp+(weather.wspd/10+weather.pres/2))/(3*weather.rhum+10*weather.prcp)
    return weather

current_weather = get_weather(Point(49.2497, -123.1193, 70), datetime.now())
current_weather = get_rel(current_weather)
print(current_weather._rel)

current_weather = get_weather(Point(30.2672, -97.7431, 489), datetime.now())
current_weather = get_rel(current_weather)
print(current_weather._rel)