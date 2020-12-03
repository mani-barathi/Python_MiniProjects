import requests				# pip install requests

# This is program will connect to a third party Weather API to fetch the current weather details of a place

# get you API KEY from https://openweathermap.org/api 
# replace you api key here
API = ''

cityName = 'chennai'		# change to your location

#API url (check  Documentation)
URL = f'http://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={API}&units=metric'

response = requests.get(URL)

print(response)

# print(response.json())

for key,value in response.json().items():
	print(f'{key} : {value}') 