from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Source, Destination
from django.template import loader
from django.utils import timezone
import pyowm

owm = pyowm.OWM('30cbc7eb4adcaf552efc6c12fa10a648')


def index(request):
    s = Source.objects.all()
    d = Destination.objects.all()
    #source = Source.objects.get(pk=source_id)
    #destination = Destination.objects.get(pk=destination_id)
    template = loader.get_template('route/index.html')
    context = {
        's': s,
        'd': d,
        'stitle': "Source cities:",
        'dtitle': "Destination cities:",
    #    'source': source,
    #    'destination': destination,
    }
    return HttpResponse(template.render(context, request))    

def detail(request, source_id, destination_id):
    return HttpResponse("You're looking at %s and %s." % (source_id, destination_id))

def temperatures(request):
    city1='chicago'
    city2='san francisco'
    selected_s = request.POST['scity']
    selected_d = request.POST['dcity']
    template = loader.get_template('route/temperatures.html')
    print selected_s, selected_d
    if selected_s == '2': city1 = 'New York'
    if selected_s == '3': city1 = 'Miami'
    if selected_s == '4': city1 = 'San Francisco'
    if selected_s == '5': city1 = 'Chicago'
    if selected_d == '1': city2 = 'New York'
    if selected_d == '2': city2 = 'Miami'
    if selected_d == '3': city2 = 'San Francisco'
    if selected_d == '4': city2 = 'Chicago'
    print city1, city2
    # Search for current weather in London (UK)
    obs1 = owm.weather_at_place(city1.lower() + ',us')
    obs2 = owm.weather_at_place(city2.lower() + ',us')
    w1 = obs1.get_weather()
    w2 = obs2.get_weather()

    # Weather details
    temp1 = w1.get_temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    temp2 = w2.get_temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    timestamp = timezone.now()
    context = {
            'city1': city1,
            'city2': city2,
            'temp1': temp1,
            'temp2': temp2,
            'timestamp': timestamp,
    }
    return HttpResponse(template.render(context, request))    

    #response = "You're looking at the temperatures at %s and %s."
    #return HttpResponse(response % (source_id, destination_id))

def routes(request):
    city1='chicago'
    city2='san francisco'
    selected_s = request.POST['scity']
    selected_d = request.POST['dcity']
    template = loader.get_template('route/routes.html')
    print selected_s, selected_d
    if selected_s == '2': city1 = 'New York, NY'
    if selected_s == '3': city1 = 'Miami, FL'
    if selected_s == '4': city1 = 'San Francisco, CA'
    if selected_s == '5': city1 = 'Chicago, IL'
    if selected_d == '1': city2 = 'New York, NY'
    if selected_d == '2': city2 = 'Miami, FL'
    if selected_d == '3': city2 = 'San Francisco, CA'
    if selected_d == '4': city2 = 'Chicago, IL'
    print city1, city2
    context = {
            'city1': city1,
            'city2': city2,
    }
    return HttpResponse(template.render(context, request))    

    #return HttpResponse("You're looking at the map route between %s and %s." % (selected_s, selected_d))
