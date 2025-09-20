from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

geolocator = Nominatim(user_agent="bits-weather-app-harshil2025-xyz@example.com")


def getweather():
    city = textfield.get()
    location = geolocator.geocode(city)
    if not location:
        timezone.config(text='City not found')
        return
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result if result else "Timezone not found")
    long_lat.config(text=f'{round(location.latitude, 4)}°N, {round(location.longitude, 4)}°E')
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')
    clock.config(text=current_time)

    api = f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&units=metric&exclude=hourly&appid=b1862ca015962bcac26feadddfbc89fc"
    json_data = requests.get(api).json()
    print(json_data)
    temp = json_data['list'][0]['main']['temp']
    humidity = json_data['list'][0]['main']['humidity']
    pressure = json_data['list'][0]['main']['pressure']
    wind = json_data['list'][0]['wind']['speed']
    description = json_data['list'][0]['weather'][0]['description']

    t.config(text=(temp, '°C'))
    h.config(text=(humidity, '%'))
    p.config(text=(pressure, 'hPa'))
    w.config(text=(wind, 'm/s'))
    d.config(text=description)

    firstdayimage = json_data['list'][0]['weather'][0]['icon']
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['list'][0]['main']['temp']
    tempfeelslike1 = json_data['list'][0]['main']['feels_like']
    day1temp.config(text=f"Temp: {tempday1}°C\n Feels like: {tempfeelslike1}°C")

    seconddayimage = json_data['list'][1]['weather'][0]['icon']
    img = (Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = round(json_data['list'][1]['main']['temp'], 1)
    day2temp.config(text=f" Temp:{tempday2}°")

    thirddayimage = json_data['list'][2]['weather'][0]['icon']
    img = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = round(json_data['list'][2]['main']['temp'], 1)
    day3temp.config(text=f" Temp:{tempday3}°")

    fourthdayimage = json_data['list'][3]['weather'][0]['icon']
    img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = round(json_data['list'][3]['main']['temp'], 1)
    day4temp.config(text=f" Temp:{tempday4}°")

    fifthdayimage = json_data['list'][4]['weather'][0]['icon']
    img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = round(json_data['list'][4]['main']['temp'], 1)
    day5temp.config(text=f" Temp:{tempday5}°")

    sixthdayimage = json_data['list'][5]['weather'][0]['icon']
    img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = round(json_data['list'][5]['main']['temp'], 1)
    day6temp.config(text=f" Temp:{tempday6}°")

    seventhdayimage = json_data['list'][6]['weather'][0]['icon']
    img = (Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = round(json_data['list'][6]['main']['temp'], 1)
    day7temp.config(text=f" Temp:{tempday7}°")

    first = datetime.now()
    day1.config(text=first.strftime(" %A"))
    second = first + timedelta(days=1)
    day2.config(text=second.strftime(" %A"))
    third = first + timedelta(days=2)
    day3.config(text=third.strftime(" %A"))
    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime(" %A"))
    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime(" %A"))
    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime(" %A"))
    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime(" %A"))


x = {'cod': '200', 'message': 0, 'cnt': 40, 'list': [{'dt': 1758358800, 'main': {'temp': 34.37, 'feels_like': 38.18, 'temp_min': 34.37, 'temp_max': 36.97, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 978, 'humidity': 47, 'temp_kf': -2.6}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 28}, 'wind': {'speed': 5.4, 'deg': 325, 'gust': 5.93}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-20 09:00:00'}, {'dt': 1758369600, 'main': {'temp': 34.54, 'feels_like': 36.66, 'temp_min': 34.54, 'temp_max': 35.27, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 978, 'humidity': 41, 'temp_kf': -0.73}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'clouds': {'all': 15}, 'wind': {'speed': 5.24, 'deg': 329, 'gust': 6.09}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-20 12:00:00'}, {'dt': 1758380400, 'main': {'temp': 32.82, 'feels_like': 34.16, 'temp_min': 32.82, 'temp_max': 32.82, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 43, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.5, 'deg': 337, 'gust': 6.84}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-20 15:00:00'}, {'dt': 1758391200, 'main': {'temp': 31.45, 'feels_like': 32.76, 'temp_min': 31.45, 'temp_max': 31.45, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 47, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.16, 'deg': 331, 'gust': 5.26}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-20 18:00:00'}, {'dt': 1758402000, 'main': {'temp': 30.41, 'feels_like': 31.5, 'temp_min': 30.41, 'temp_max': 30.41, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 49, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.73, 'deg': 286, 'gust': 3.74}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-20 21:00:00'}, {'dt': 1758412800, 'main': {'temp': 29.55, 'feels_like': 30.54, 'temp_min': 29.55, 'temp_max': 29.55, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 51, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.76, 'deg': 298, 'gust': 3.98}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-21 00:00:00'}, {'dt': 1758423600, 'main': {'temp': 31.54, 'feels_like': 32.33, 'temp_min': 31.54, 'temp_max': 31.54, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 980, 'humidity': 44, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.97, 'deg': 284, 'gust': 3.52}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-21 03:00:00'}, {'dt': 1758434400, 'main': {'temp': 36.08, 'feels_like': 36.29, 'temp_min': 36.08, 'temp_max': 36.08, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 30, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.69, 'deg': 299, 'gust': 7.74}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-21 06:00:00'}, {'dt': 1758445200, 'main': {'temp': 37.87, 'feels_like': 37.71, 'temp_min': 37.87, 'temp_max': 37.87, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 25, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 6.17, 'deg': 314, 'gust': 7.52}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-21 09:00:00'}, {'dt': 1758456000, 'main': {'temp': 35.88, 'feels_like': 35.51, 'temp_min': 35.88, 'temp_max': 35.88, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 28, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.35, 'deg': 323, 'gust': 7.05}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-21 12:00:00'}, {'dt': 1758466800, 'main': {'temp': 33.16, 'feels_like': 33.82, 'temp_min': 33.16, 'temp_max': 33.16, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.16, 'deg': 350, 'gust': 7.11}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-21 15:00:00'}, {'dt': 1758477600, 'main': {'temp': 31.54, 'feels_like': 32.33, 'temp_min': 31.54, 'temp_max': 31.54, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 44, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.48, 'deg': 301, 'gust': 3.3}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-21 18:00:00'}, {'dt': 1758488400, 'main': {'temp': 30.85, 'feels_like': 31.48, 'temp_min': 30.85, 'temp_max': 30.85, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 45, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.17, 'deg': 282, 'gust': 4.87}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-21 21:00:00'}, {'dt': 1758499200, 'main': {'temp': 30.17, 'feels_like': 30.14, 'temp_min': 30.17, 'temp_max': 30.17, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 42, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.25, 'deg': 274, 'gust': 8.93}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-22 00:00:00'}, {'dt': 1758510000, 'main': {'temp': 32.22, 'feels_like': 31.46, 'temp_min': 32.22, 'temp_max': 32.22, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 980, 'humidity': 33, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.17, 'deg': 288, 'gust': 10.16}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-22 03:00:00'}, {'dt': 1758520800, 'main': {'temp': 36.15, 'feels_like': 35.25, 'temp_min': 36.15, 'temp_max': 36.15, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 980, 'humidity': 25, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.9, 'deg': 298, 'gust': 8.26}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-22 06:00:00'}, {'dt': 1758531600, 'main': {'temp': 37.66, 'feels_like': 36.89, 'temp_min': 37.66, 'temp_max': 37.66, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 23, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.78, 'deg': 310, 'gust': 6.93}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-22 09:00:00'}, {'dt': 1758542400, 'main': {'temp': 36.19, 'feels_like': 35.52, 'temp_min': 36.19, 'temp_max': 36.19, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 26, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.95, 'deg': 320, 'gust': 6.71}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-22 12:00:00'}, {'dt': 1758553200, 'main': {'temp': 33.43, 'feels_like': 33.61, 'temp_min': 33.43, 'temp_max': 33.43, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 36, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.64, 'deg': 344, 'gust': 5.22}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-22 15:00:00'}, {'dt': 1758564000, 'main': {'temp': 32.02, 'feels_like': 32.31, 'temp_min': 32.02, 'temp_max': 32.02, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 40, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 1.53, 'deg': 303, 'gust': 3.23}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-22 18:00:00'}, {'dt': 1758574800, 'main': {'temp': 31.24, 'feels_like': 31.08, 'temp_min': 31.24, 'temp_max': 31.24, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.18, 'deg': 275, 'gust': 5.97}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-22 21:00:00'}, {'dt': 1758585600, 'main': {'temp': 29.84, 'feels_like': 29.29, 'temp_min': 29.84, 'temp_max': 29.84, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 38, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 3.54, 'deg': 283, 'gust': 9.72}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-23 00:00:00'}, {'dt': 1758596400, 'main': {'temp': 31.79, 'feels_like': 31.2, 'temp_min': 31.79, 'temp_max': 31.79, 'pressure': 1006, 'sea_level': 1006, 'grnd_level': 980, 'humidity': 35, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.28, 'deg': 286, 'gust': 9.49}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-23 03:00:00'}, {'dt': 1758607200, 'main': {'temp': 35.79, 'feels_like': 34.41, 'temp_min': 35.79, 'temp_max': 35.79, 'pressure': 1005, 'sea_level': 1005, 'grnd_level': 980, 'humidity': 23, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.58, 'deg': 302, 'gust': 7.09}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-23 06:00:00'}, {'dt': 1758618000, 'main': {'temp': 37.34, 'feels_like': 36.23, 'temp_min': 37.34, 'temp_max': 37.34, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 22, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.2, 'deg': 306, 'gust': 6.24}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-23 09:00:00'}, {'dt': 1758628800, 'main': {'temp': 36.04, 'feels_like': 34.91, 'temp_min': 36.04, 'temp_max': 36.04, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 976, 'humidity': 24, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.89, 'deg': 310, 'gust': 6.69}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-23 12:00:00'}, {'dt': 1758639600, 'main': {'temp': 33.61, 'feels_like': 33.29, 'temp_min': 33.61, 'temp_max': 33.61, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 33, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.41, 'deg': 335, 'gust': 5.49}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-23 15:00:00'}, {'dt': 1758650400, 'main': {'temp': 32.06, 'feels_like': 31.85, 'temp_min': 32.06, 'temp_max': 32.06, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 977, 'humidity': 37, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.23, 'deg': 285, 'gust': 4.92}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-23 18:00:00'}, {'dt': 1758661200, 'main': {'temp': 30.84, 'feels_like': 30.57, 'temp_min': 30.84, 'temp_max': 30.84, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.16, 'deg': 276, 'gust': 10.8}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-23 21:00:00'}, {'dt': 1758672000, 'main': {'temp': 29.61, 'feels_like': 29.7, 'temp_min': 29.61, 'temp_max': 29.61, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 44, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.46, 'deg': 280, 'gust': 10.68}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-24 00:00:00'}, {'dt': 1758682800, 'main': {'temp': 30.45, 'feels_like': 30.49, 'temp_min': 30.45, 'temp_max': 30.45, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 979, 'humidity': 42, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.46, 'deg': 288, 'gust': 9.8}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-24 03:00:00'}, {'dt': 1758693600, 'main': {'temp': 34.74, 'feels_like': 34.94, 'temp_min': 34.74, 'temp_max': 34.74, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 33, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.3, 'deg': 296, 'gust': 6.83}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-24 06:00:00'}, {'dt': 1758704400, 'main': {'temp': 36.86, 'feels_like': 36.98, 'temp_min': 36.86, 'temp_max': 36.86, 'pressure': 1000, 'sea_level': 1000, 'grnd_level': 976, 'humidity': 28, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 5.2, 'deg': 301, 'gust': 6.09}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-24 09:00:00'}, {'dt': 1758715200, 'main': {'temp': 35.65, 'feels_like': 35.87, 'temp_min': 35.65, 'temp_max': 35.65, 'pressure': 999, 'sea_level': 999, 'grnd_level': 975, 'humidity': 31, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.99, 'deg': 303, 'gust': 6.15}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-24 12:00:00'}, {'dt': 1758726000, 'main': {'temp': 33.49, 'feels_like': 34.34, 'temp_min': 33.49, 'temp_max': 33.49, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 976, 'humidity': 39, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.85, 'deg': 327, 'gust': 5.89}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-24 15:00:00'}, {'dt': 1758736800, 'main': {'temp': 31.91, 'feels_like': 32.9, 'temp_min': 31.91, 'temp_max': 31.91, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 976, 'humidity': 44, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 2.23, 'deg': 283, 'gust': 4.24}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-24 18:00:00'}, {'dt': 1758747600, 'main': {'temp': 30.8, 'feels_like': 30.27, 'temp_min': 30.8, 'temp_max': 30.8, 'pressure': 1001, 'sea_level': 1001, 'grnd_level': 976, 'humidity': 37, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.05, 'deg': 280, 'gust': 10.13}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-24 21:00:00'}, {'dt': 1758758400, 'main': {'temp': 29.31, 'feels_like': 29.46, 'temp_min': 29.31, 'temp_max': 29.31, 'pressure': 1002, 'sea_level': 1002, 'grnd_level': 977, 'humidity': 45, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.25, 'deg': 280, 'gust': 10.22}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'n'}, 'dt_txt': '2025-09-25 00:00:00'}, {'dt': 1758769200, 'main': {'temp': 30.32, 'feels_like': 30.6, 'temp_min': 30.32, 'temp_max': 30.32, 'pressure': 1004, 'sea_level': 1004, 'grnd_level': 978, 'humidity': 44, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.95, 'deg': 288, 'gust': 8.7}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-25 03:00:00'}, {'dt': 1758780000, 'main': {'temp': 34.38, 'feels_like': 34.84, 'temp_min': 34.38, 'temp_max': 34.38, 'pressure': 1003, 'sea_level': 1003, 'grnd_level': 978, 'humidity': 35, 'temp_kf': 0}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': {'all': 0}, 'wind': {'speed': 4.83, 'deg': 299, 'gust': 5.85}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2025-09-25 06:00:00'}], 'city': {'id': 1273840, 'name': 'Connaught Place', 'coord': {'lat': 28.6328, 'lon': 77.2198}, 'country': 'IN', 'population': 0, 'timezone': 19800, 'sunrise': 1758328708, 'sunset': 1758372653}}

root = Tk()
root.title("Weather App")
root.geometry("900x470+300+200")
root.configure(bg='#57adff')
root.resizable(False, False)

image_icon = PhotoImage(file='Images/logo.png')
root.iconphoto(False, image_icon)

round_box = PhotoImage(file='Images/Rounded Rectangle 1.png')
Label(root, image=round_box, bg='#57adff').place(x=30, y=110)

label1 = Label(root, text='Temperature', font=('Helvetica', 11), fg='white', bg='#203243')
label1.place(x=50, y=120)

label2 = Label(root, text='Humidity', font=('Helvetica', 11), fg='white', bg='#203243')
label2.place(x=50, y=140)

label3 = Label(root, text='Pressure', font=('Helvetica', 11), fg='white', bg='#203243')
label3.place(x=50, y=160)

label4 = Label(root, text='Wind Speed', font=('Helvetica', 11), fg='white', bg='#203243')
label4.place(x=50, y=180)

label5 = Label(root, text='Description', font=('Helvetica', 11), fg='white', bg='#203243')
label5.place(x=50, y=200)

search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=search_image, bg='#57adff')
myimage.place(x=270, y=120)

weat_image = PhotoImage(file='Images/Layer 7.png')
weatherimage = Label(root, image=weat_image, bg='#203243')
weatherimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg='#203243', border=0, fg='white')
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(image=search_icon, borderwidth=0, cursor="hand2", bg='#203243', command=getweather)
myimage_icon.place(x=645, y=125)

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg='#212120').place(x=30, y=20)
Label(frame, image=secondbox, bg='#212120').place(x=300, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=400, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=500, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=600, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=700, y=30)
Label(frame, image=secondbox, bg='#212120').place(x=800, y=30)

clock = Label(root, font=('Helvetica', 30, 'bold'), fg='white', bg='#57adff')
clock.place(x=30, y=20)

timezone = Label(root, font=('Helvetica', 20), fg='white', bg='#57adff')
timezone.place(x=700, y=20)

long_lat = Label(root, font=('Helvetica', 10), fg='white', bg='#57adff')
long_lat.place(x=700, y=50)

t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)

# first box
firstframe = Frame(root, width=230, height=132, bg='#282829')
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font='arial 15', bg='#282829', fg='#fff')
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg='#282829')
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=90, y=50)

# second box
secondframe = Frame(root, width=70, height=115, bg='#282829')
secondframe.place(x=305, y=325)

day2 = Label(secondframe, font='arial 15', bg='#282829', fg='#fff')
day2.place(x=0, y=5)

secondimage = Label(secondframe, bg='#282829')
secondimage.place(x=7, y=30)

day2temp = Label(secondframe, bg="#282829", fg="#fff")
day2temp.place(x=0, y=80)

# third box
thirdframe = Frame(root, width=70, height=115, bg='#282829')
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, font='arial 15', bg='#282829', fg='#fff')
day3.place(x=0, y=5)

thirdimage = Label(thirdframe, bg='#282829')
thirdimage.place(x=7, y=30)

day3temp = Label(thirdframe, bg="#282829", fg="#fff")
day3temp.place(x=0, y=80)

# fourth box
fourthframe = Frame(root, width=70, height=115, bg='#282829')
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, font='arial 15', bg='#282829', fg='#fff')
day4.place(x=0, y=5)

fourthimage = Label(fourthframe, bg='#282829')
fourthimage.place(x=7, y=30)

day4temp = Label(fourthframe, bg="#282829", fg="#fff")
day4temp.place(x=0, y=80)

# fifth box
fifthframe = Frame(root, width=70, height=115, bg='#282829')
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, font='arial 15', bg='#282829', fg='#fff')
day5.place(x=0, y=5)

fifthimage = Label(fifthframe, bg='#282829')
fifthimage.place(x=7, y=30)

day5temp = Label(fifthframe, bg="#282829", fg="#fff")
day5temp.place(x=0, y=80)

# sixth box
sixthframe = Frame(root, width=70, height=115, bg='#282829')
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, font='arial 15', bg='#282829', fg='#fff')
day6.place(x=0, y=5)

sixthimage = Label(sixthframe, bg='#282829')
sixthimage.place(x=7, y=30)

day6temp = Label(sixthframe, bg="#282829", fg="#fff")
day6temp.place(x=0, y=80)

# seventh box
seventhframe = Frame(root, width=70, height=115, bg='#282829')
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, font='arial 15', bg='#282829', fg='#fff')
day7.place(x=0, y=5)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=7, y=30)

day7temp = Label(seventhframe, bg="#282829", fg="#fff")
day7temp.place(x=0, y=80)

root.mainloop()
