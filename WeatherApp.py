import tkinter as tk
import requests
from tkinter import font
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

# 6ee6fe36a7673be34c676f367f584873

# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}

def get_weather(city):
    weather_key = '6ee6fe36a7673be34c676f367f584873'
    # connecting to the API using the url and params below
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    # returning the requested queries and printing in dict. format
    response = requests.get(url, params= params)
    weather = response.json()

    label['text'] = format_response(weather)

    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def format_response(weather):
    try:
        # Get the name of the requested location
        name = f"{weather['name']}, {weather['sys']['country']}"
        desc = f"Weather: {weather['weather'][0]['description']}"
        temp = f"Temperature: {weather['main']['temp']}°C but it feels like: {weather['main']['feels_like']}°C"
        min_max = f"Min Temp: {weather['main']['temp_min']}°C, Max Temp: {weather['main']['temp_max']}°C"

        final_str = f"{name} \n{desc} \n{temp} \n{min_max}"
    except:
        final_str = "Request could not be processed. Please try again!"

    return final_str


def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='weather_app_bg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

upper_frame = tk.Frame(root, bg="#80c1ff", bd=5)
# This sets the relative height and width of the frame and also its position.
# it is centered around the middle of the screen and at 10% from the top of the frame.
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(upper_frame, font=('MS Sans Serif', 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(upper_frame, text='Get Weather', font=('Terminal', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Terminal',10))
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
