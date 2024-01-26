from urllib.request import urlopen 
import json

url = urlopen("https://api.open-meteo.com/v1/forecast?latitude=51.5002&longitude=-0.1262&current_weather=true")
response = url.read().decode('UTF-8')
print(response)

json_data = json.loads(response)
print(json_data['current_weather'])
