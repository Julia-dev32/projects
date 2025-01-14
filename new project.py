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

    weather_city.config(text=city.capitalize())
    weather_temp.config(text=f"{temp * 9/5 + 32:.0f}°F")
    weather_description.config(text=weather_desc)

    if "rain" or "mist" in weather_desc:
        Image_path = "/Users/juliarodriguez/Desktop/rain.png"
    elif any(keyword in weather_desc for keyword in ["cloud", "clouds", "cloudy"]):
        Image_path = "/Users/juliarodriguez/Desktop/clouds.png"
    elif "snow" or "snowing" in weather_desc:
        Image_path = "/Users/juliarodriguez/Desktop/snow.png"
    elif any(keyword in weather_desc for keyword in ["sunny", "clear", "sun"]):
        Image_path = "/Users/juliarodriguez/Desktop/sun.png"



    photo = Image.open(Image_path)
    photo = photo.resize((400, 300))
    photo = ImageTk.PhotoImage(photo)
    image_label.config(image=photo)
    

    city_entry.grid_forget()
    city_label.grid_forget()
    back_button.grid_forget()

def reset_to_search():
    city_label.grid(row=0, column=0, padx=5, pady=5)
    city_entry.grid(row=0, column=1,padx=15, pady=15)

    weather_city.config(text="")
    weather_description.config(text="")
    weather_temp.config(text="")
    image_label.config(Image=None)

    city_entry.focus()


def ui_setup():
    global city_label, city_entry, weather_city, weather_temp, weather_description, root, image_label, back_button
    root = tk.Tk()
    root.title("Weather App")
    root.minsize(300, 600)
    root.configure(bg="pink")
    root.update_idletasks()

    dark_purple = '#5D2F8E'

    city_label = tk.Label(root, text="City Search", font=("Futura", 45), fg=dark_purple, bg= "pink")
    city_label.grid(row=0, column=0, padx=5, pady=5)
    city_entry = tk.Entry(root, font=("Futura", 45), bg="light grey",  width=15, fg=dark_purple)
    city_entry.grid(row=0, column=1,padx=15, pady=15)

    city_entry.bind("<Return>", get_weather)


    weather_city = tk.Label(root,font=("Futura", 55), fg=dark_purple, bg="pink")
    weather_city.place(relx=0.5, rely=0.09, anchor="center")

    weather_temp = tk.Label(root,font=("Futura", 65), fg=dark_purple, bg="pink")
    weather_temp.place(relx=0.5, rely=0.21, anchor="center")

    weather_description = tk.Label(root, font=("Futura",35), fg=dark_purple, bg="pink")
    weather_description.place(relx=0.5, rely=0.31, anchor="center")
 
    image_label = tk.Label(root, bg="pink")
    image_label.place(relx=0.5, rely=0.71, anchor="center")
    
    back_button = tk.Button(root, text="Back", font=("Futura",25), fg=dark_purple, bg="pink", command=reset_to_search)
    back_button.place(relx=0.15, rely=0.10, anchor="center")
    root.mainloop()
ui_setup()



