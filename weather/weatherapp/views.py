from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import pprint
from datetime import datetime


# Create your views here.
front  = "https://api.darksky.net/forecast/a8f6a79f78270a75d1bca5903b770284/"
back = "?exclude=[hourly,flags,alerts,minutely,daily]?units=[si]"


location1 = "-33.927407,18.415747"
location2 = "-38.927407,45.415747"



def currentWeather(location1):
    current = front + location1 + back
    response1 = requests.get(current)
    text1 = response1.json()
    #pprint.pprint(text1)

    date = response1.json()['currently']['time']
    time = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

    day = response1.json()['currently']['icon']

    desc = response1.json()['currently']['summary']

    temp = response1.json()['currently']['temperature']
    temp = (temp-32)*5/9
    #print("{:.1f}".format(temp))

    windspd = response1.json()['currently']['windSpeed']  

    windgst = response1.json()['currently']['windGust'] 

    windbrng = response1.json()['currently']['windBearing']

    rainprb = response1.json()['currently']['precipProbability']

    longi = response1.json()['longitude']

    lati = response1.json()['latitude']

    arr1 = [time, day, desc, temp, windspd, windgst, windbrng, rainprb, longi, lati]

    return(arr1)

def bookingWeather(location2):

    booking = front + location2 + back

    response2 = requests.get(booking)
    text1 = response2.json()
    #text2 = response2.json()
    #pprint.pprint(text1)
    #pprint.pprint(text2)

    date = response2.json()['currently']['time']
    time = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

    day = response2.json()['currently']['icon']

    desc = response2.json()['currently']['summary']

    temp = response2.json()['currently']['temperature']
    temp = (temp-32)*5/9
    #print("{:.1f}".format(temp))

    windspd = response2.json()['currently']['windSpeed']  

    windgst = response2.json()['currently']['windGust'] 

    windbrng = response2.json()['currently']['windBearing']

    rainprb = response2.json()['currently']['precipProbability']

    longi = response2.json()['longitude']

    lati = response2.json()['latitude']

    arr1 = [time, day, desc, temp, windspd, windgst, windbrng, rainprb, longi, lati]

    return(arr1)


import sys
sys.path.insert(0, "C:\\Users\\micha_000\\Desktop\\programming\\sweepsouth\\weather")

import os
os.chdir("C:\\Users\\micha_000\\Desktop\\programming\\sweepsouth\\weather")
os.environ['DJANGO_SETTINGS_MODULE'] = 'weather.settings'

import weatherapp.models as w
#print(currentWeather(location1))

o = w.CurrentLocation()
k = currentWeather(location1)
o.date = k[0]
o.typeday = k[1]
o.desc = k[2]
o.temp = k[3]
o.windspeed = k[4]
o.windbearing = k[5]
o.windgust = k[6]
o.rain_prob = k[7]
o.latitude = k[8]
o.longitude = k[9]
o.save()

import weatherapp.models as w
o = w.BookingLocation()
k = bookingWeather(location1)
o.date = k[0]
o.typeday = k[1]
o.desc = k[2]
o.temp = k[3]
o.windspeed = k[4]
o.windbearing = k[5]
o.windgust = k[6]
o.rain_prob = k[7]
o.latitude = k[8]
o.longitude = k[9]
o.save()


print(w.BookingLocation.objects.all())

