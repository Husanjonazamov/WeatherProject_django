from django.shortcuts import render
import requests
import datetime

def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
        if 'city' == 'weather':
            return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'time': time, 'city': city})
        else:
            city = request.POST['city']
    else:
        city = 'Uzbekistan'


    appid = 'b9b3259a967be4901ce59d9a03ac0d8e'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {
        'q': city,
        'appid': appid,
        'units': 'metric',
    }
    r = requests.get(url=URL, params=PARAMS)
    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']
    day = datetime.date.today()
    time = datetime.time()
    return render(request, 'weatherapp/index.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day, 'time': time, 'city': city})


