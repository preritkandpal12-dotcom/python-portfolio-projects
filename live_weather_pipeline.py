import requests
url = url = "https://api.open-meteo.com/v1/forecast?latitude=16.6568&longitude=73.517&current_weather=true"
print("Sending HTTP GET Request to Open-Meteo Servers...")
response = requests.get(url)
print(f"Server response code: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    current = data['current_weather']
    print(f"Current Temperature: {current['temperature']}°C")
    print(f"Wind Speed: {current['windspeed']} km/hr")
else:
    print("Network pipeline failed to fetch live data")
    

      
