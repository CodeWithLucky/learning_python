import requests

lat = 12.2
lon = 13.7
apiKey = '1bf779b770c0a107b0cce8a6eec0f09c'

print("...WEATHER APP...")
userCity = input("Enter your city   ").lower()

try:
    city = 'kathmandu'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={userCity}&units=metric&appid={apiKey}'

    response = requests.get(url.format(city)).json()


     
    # print(response)

except requests.RequestException as e:
    print("Request failed:", e)



value1 = response['weather']
tempretures = response['main']
city = response['name']
country = response['sys']

print(f"...{userCity}, {country['country']} weather report...")
print(f"Current tempreture {tempretures['temp']}\n Feels like {tempretures['feels_like']}\n Maximum temptreture {tempretures['temp_max']}\n Minimum tempreture {tempretures['temp_min']}\n Humidity {tempretures['humidity']}")



