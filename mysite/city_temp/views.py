from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import gviz_api
import datetime
import mraa
import time
import sys
import math
import pyowm

owm = pyowm.OWM('30cbc7eb4adcaf552efc6c12fa10a648')
# Create your views here.

def index(request):
    tempSensor_pin_number = 1
 
    # Configuring the switch and temperature Sencor as GPIO interfaces
    tempSensor = mraa.Aio(tempSensor_pin_number)
 
    # Configuring the switch and buzzer as input & output respectively
    reading = tempSensor.read()
    r = 100000*(float(1023/float(reading)) - 1)
    temperatureC = (1/(math.log(r/100000.0)/4275 + (1/298.15))) - 273.15
    edison = "%.4f" % temperatureC
    observation = owm.weather_at_place('new york,us')
    w = observation.get_weather()
    pyowmtemp = w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

    template = loader.get_template('city_temp/index.html')
    context = {
        'edison': float(edison),
        'temp_max': float(pyowmtemp['temp_max']),
        'temp_min': float(pyowmtemp['temp_min']),
        'temp': float(pyowmtemp['temp']),
        'av_temp': (float(edison) + float(pyowmtemp['temp_max']) + float(pyowmtemp['temp_max']) + float(pyowmtemp['temp_max']))/4,
    }
    return HttpResponse(template.render(context, request))    
    #return HttpResponse("Welcome to the city temperature app.")

