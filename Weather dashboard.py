import requests

def main():
    api_key = "492215b8ff874d2e62fcbdf5020e0e03"

    user_lat = input("Enter Lattitude: ")
    user_long = input("Enter Longitude: ")
    weatherdata(user_lat, user_long, api_key)

def weatherdata(user_lat, user_long, api_key):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={user_lat}&lon={user_long}&appid={api_key}")
    
main()