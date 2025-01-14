import tkinter as tk 
from tkinter import ttk
import requests
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os

def get_weather(event=None):
    city = city_entry.get()
    
    if not city:
        print("Input Error, please enter a valid city")
        return
    
    api_key = "492215b8ff874d2e62fcbdf5020e0e03"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"API Error: {response.json().get('message', 'Unknown error')}")
        return
    
    data = response.json()

    if "main" not in data or "weather" not in data or "wind" not in data:
        print("Invalid data received from the API.")
        return
    
    temp = data["main"]["temp"]
    weather_desc = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    weather_city.config(text=city)
    weather_temp.config(text=f"{temp * 9/5 + 32:.0f}°F")
    weather_description.config(text=weather_desc)

   
    city_entry.destroy()
    city_label.destroy()

def ui_setup():
    global city_label, city_entry, weather_city, weather_temp, weather_description, root
    root = tk.Tk()
    root.title("Weather App")
    root.minsize(300, 600)
    root.configure(bg="pink")
    root.update_idletasks()

    dark_purple = '#5D2F8E'

    anime_font = ("Futura", 45)
    city_label = tk.Label(root, text="City Search", font=anime_font, fg=dark_purple, bg= "pink")
    city_label.grid(row=0, column=0, padx=5, pady=5)
    city_entry = tk.Entry(root, font=anime_font, bg="light grey",  width=15, fg=dark_purple)
    city_entry.grid(row=0, column=1,padx=15, pady=15)

    city_entry.bind("<Return>", get_weather)


    weather_city = tk.Label(root,font=("Futura", 55), fg=dark_purple, bg="pink")
    weather_city.place(relx=0.5, rely=0.09, anchor="center")

    weather_temp = tk.Label(root,font=("Futura", 65), fg=dark_purple, bg="pink")
    weather_temp.place(relx=0.5, rely=0.21, anchor="center")

    weather_description = tk.Label(root, font=("Futura",35), fg=dark_purple, bg="pink")
    weather_description.place(relx=0.5, rely=0.31, anchor="center")

    image = Image.open()

    root.mainloop()
ui_setup()