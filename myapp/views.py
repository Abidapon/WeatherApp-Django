from django.shortcuts import render
import requests
from .forms import CitySearchForm

def get_weather_data(city):

    api_key = '68fa0629860a793b27233d6556b032a0'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def index(request):
    if request.method == 'GET':
        form = CitySearchForm(request.GET)
    else:
        form = CitySearchForm()

    if form.is_valid():
        city = form.cleaned_data['city']
        weather_data = get_weather_data(city)

        if 'main' in weather_data:
            # Valid data received
            context = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
            }
        else:
            context = {
                'form': form,
                'error_message': 'Invalid city name. Please enter a valid city.',
            }
    else:
        # Handle invalid form input
        context = {'form': form}

    return render(request, 'weatherapp/index.html', context)
