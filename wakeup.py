import requests
from datetime import datetime
import random


def getWeather():
    now = datetime.strftime(datetime.now(), "%A, %b %d %I:%S %p")
    lat = '41.120471'
    lon = '-73.590573'
    # print(loc['latitude'],loc['longitude'])
    r = requests.get(
        f"https://api.darksky.net/forecast/{apikey}/{lat},{lon}")
    req = r.json()
    current = req['currently']
    # print(req['hourly'])
    currhumidity = int(current['humidity'] * 100)
    curreport = f"It's currently {now}, {current['apparentTemperature']} degrees and {(current['summary']).lower()}" \
        f" with {currhumidity}% humidity"
    if current['precipProbability'] > 25:
        currprecip = current['precipProbability'] * 100
        curreport += f"There is a f{currprecip} chance of rain "
    # print(curreport)
    todayreport = f"and it will be {req['hourly']['summary']}".lower()
    # print(todayreport)
    return curreport, todayreport


def getTodayinHistory():
    random.seed()
    r = requests.get("https://history.muffinlabs.com/date")
    rson = r.json()
    rmax = len(rson['data']['Events'])
    ind = random.randrange(0, rmax + 1)
    fact = rson['data']['Events'][ind]['text']
    yr = rson['data']['Events'][ind]['year']
    todayinh = f"In {yr}, {fact}."
    return todayinh


if __name__ == "__main__":
    # getCalendar()
    curr, summ = getWeather()
    ttd = getTodayinHistory()
    print(f"{curr} {summ}\n{ttd}")
