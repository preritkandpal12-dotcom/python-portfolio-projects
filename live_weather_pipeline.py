import requests
import pandas as pd
from datetime import datetime

# CONSTANTS
CITIES = {
    "mumbai": {"lat": 19.0760, "lon": 72.877},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "new york": {"lat": 40.7128, "lon": -74.0060}
}

def fetch_weather_data(city_name, coords):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"
    
    try:
  
        response = requests.get(url)
        response.raise_for_status() 
        
        current = response.json()['current_weather']
        weather_dict = {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M")],
            "City": [city_name.title()],
            "Temperature (C)": [current['temperature']],
            "Wind Speed (km/hr)": [current['windspeed']]
        }
        return weather_dict
        
    except requests.exceptions.RequestException as e:
        print(f" Network failure for {city_name.title()}: Server unreachable.")
        return None

def save_to_csv(weather_dict):
    df = pd.DataFrame(weather_dict)
    df.to_csv("my_weather_log.csv", mode='a', index=False, header=False)
    print(f" Saved data for {weather_dict['City'][0]}")

def run_pipeline():
    print("\n Initiating bulletproof batch weather fetch...")
    
    for city_name, coords in CITIES.items():
        weather_data = fetch_weather_data(city_name, coords)
        
        if weather_data is not None:
            save_to_csv(weather_data)
            
    print(" Pipeline execution complete!\n")

if __name__ == "__main__":
    run_pipeline()




         

