import requests
import pandas as pd 
from datetime import datetime 

CITIES = { 
    "mumbai": {"lat": 19.0760, "lon": 72.877},
    "london": {"lat": 51.5074, "lon": -0.1278},
    "new york": {"lat": 40.7128, "lon": -74.0060}
}
print("\n Initiating automated batch weather fetch...")
for city_name, coords in CITIES.items():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current_weather=true"

    print(f"Connecting to grid for {city_name .title()}...")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current = data['current_weather']

        weather_dict = {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M")],
            "City": [city_name.title()],
            "Temperature (c)": [current['temperature']],
            "Wind speed (km/hr)": [current['windspeed']]
        }

        df = pd.DataFrame(weather_dict)

        df.to_csv("my_weather_log.csv", mode = 'a', index=False, header=False)
    else:
        print(f"Failed to fetch data for {city_name.title() }")
print("Batch process complete!\n")




         

