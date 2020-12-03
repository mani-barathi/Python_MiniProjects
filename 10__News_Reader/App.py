import requests     # pip install requests
import pyttsx3      # pip install pyttsx3

# generate your API KEY from https://newsapi.org/
# replace your key here
API = ''


# change country as per your location
COUNTRY = 'in'
URL = f'http://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={API}'

# no of news articles to be fetched, change as per you requirement
total=5

# initializing text to speech engine
print(f'Starting voice engine...')
engine = pyttsx3.init()

# changing the speeking rate  
engine.setProperty('rate',140)  

#changing the voice to female voice
voices = engine.getProperty('voices')    
engine.setProperty('voice', voices[1].id) 

# making  request to API
print(f'Fetching news from API... \n')
response = requests.get(URL)
# print(response.json())
print("-"*40)

# converting response to json object
data=response.json()['articles'] 
# keys which I need to extract from json object
my_needs=['title','description','url']

for i in range(total):
    print("NEWS",i+1)
    for key,value in data[i].items():
        if key in my_needs:							# checking if the current key is a needed key
            if key=='title':
                value=value.split('-')[0]
            
            if key in ['title','url'] :
                print(key.upper()," : ",value)
                
            if key in ['title','description']:		# we want engine to speak only title and description
                engine.say(f'news {i+1} {key}')
                engine.runAndWait()					# to make the speech engine to wait for a moment and then continue
                engine.say(value)
                engine.runAndWait()
    print("-"*40)
    print()

input('Press enter to exit ')
print('Thank you :)')
