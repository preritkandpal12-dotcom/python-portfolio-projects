import requests
import pandas as pd
from datetime import datetime 
CITIES = {
    "mumbai": {"lat": 19.0760, "lon": 72.877},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "new york": {"lat": 40.7128, "lon": -74.0060}
}

user_choice = input("Enter a city (Mumbai, London, New york): ").strip().lower() 

if user_choice in CITIES:
    coords = CITIES[user_choice]

url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"

print(f"\nConnecting to weather grid for {user_choice.title()}...")
response = requests.get(url)

print(f"Server response code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    current = data['current_weather']

    print(f"Current Temperature: {current['temperature']}°C")
    print(f"Wind Speed: {current['windspeed']} km/hr")
    weather_dict = { 
        "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "City": [user_choice .title()],
        "Temperature (C)": [current ['temperature']],
        "Wind Speed (km/hr)": [current['windspeed']]
        
    }

    df= pd.DataFrame(weather_dict)
    df.to_csv("my_weather_log.csv" , mode='a' , index = False , header=False)
    print("\n Live data succesfully saved to my_weather_log.csv ")
else:
    print("Network pipeline failed to fetch live data")
    

      
