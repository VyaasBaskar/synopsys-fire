import meteostat
from meteostat import Point, Hourly
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def get_weather(location, time):
    data = Hourly(location, time-timedelta(1/24, 0), time)
    data = data.fetch()
    return (data["temp"], data["rhum"], data["wdir"], data["wspd"], data["pres"], data["prcp"])
print(get_weather(Point(49.2497, -123.1193, 70), datetime.now()))