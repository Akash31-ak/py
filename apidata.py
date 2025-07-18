#Web API
import pandas as pd
import json
#convert python dict to json
data ={
    'name':"Alice",
    'college':"PU"
}
json_str = json.dumps(data)#json.dumps
# print(json_str)

# df = pd.read_json("titanic.json",lines=True)
# print(df.head(10))
# #convert json string to python dict
# json_data = """{
#     "PassengerId":"1",
#     "Survived":"0",
#     "Pclass":"3",
#     "Name":"Braund,Mr.Owen Harris",
#     "Sex":"male",
#     "Age":22
# }"""
# data1 = json.loads(json_data)#converts json str to dict
# print(data1["Name"])

#py -m pip install requests
import requests
api_key = "ZeP1hrM01uKdYPnMlfwnDMrv12xLWN82"#to be replaced 
city = input("Enter the city:")
url = f"http://dataservice.accuweather.com/locations/v1/cities/search?q={city}&apikey={api_key}"
def fetchLocation():
    location_url = url
    response = requests.get(location_url)
    data = response.json()
    if response.status_code==200 and data:
        location_key = data[0]['Key']
        return location_key
    else:
        print("Error fetching the data")

location_key =fetchLocation()
weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"

response = requests.get(weather_url)
if response.status_code==200:
    weather_data = response.json()
    if weather_data:
        temperature = weather_data[0]['Temperature']['Metric']['Value']
        unit = weather_data[0]['Temperature']['Metric']['Unit']
        description = weather_data[0]['WeatherText']
        print(f"Current weather in {city}: {description}, {temperature} degree {unit}")
    else:
        print("No weather data found")
else:
    print(f"Failed to fetch weather.status:{response.status_code}"())


