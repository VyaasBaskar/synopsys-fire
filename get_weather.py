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
    T_CO = 4
    WS_CO = 1/10
    WP_CO = 1/2
    H_CO = 3
    P_CO = 10
    weather._rel = (T_CO*weather.temp+(weather.wspd*WS_CO+weather.pres*WP_CO))/(H_CO*weather.rhum+P_CO*weather.prcp)
    return weather

current_weather = get_weather(Point(49.2497, -123.1193, 70), datetime.now())
current_weather = get_rel(current_weather)
print(current_weather._rel)

current_weather = get_weather(Point(30.2672, -97.7431, 489), datetime.now())
current_weather = get_rel(current_weather)
print(current_weather._rel)