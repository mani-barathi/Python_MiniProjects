from bs4 import BeautifulSoup
import requests

ID=input("Enter a Instagram ID: ")

if ID.startswith('@'):
	ID=ID[1:]

# requesting the instagram site 
IG=requests.get(f'https://www.instagram.com/{ID}/')
IG_code=IG.text

# passing the instagram page source code to bs4 object
soup=BeautifulSoup(IG_code,'lxml')
# print(soup)
#saving the name from the webpage
name=soup.title.text.split("(")[0].strip()

# getting the details of followers,following and posts
metatag=soup.find('meta',property='og:description')
info=(metatag["content"]).replace(',','')
info=info.split(' ')

# getting the url which points to the instagram's profile pic of the user
image=soup.find('meta',property="og:image")
img_url=image["content"]
# requesting the profile pic url 
profile_pic=requests.get(img_url)

# saving the image to system 
with open(f'{ID}.jpg','wb') as f:
	f.write(profile_pic.content)
	print(f'{ID}.jpg Downloaded')

# creating a dictionary out of all information
data={
	'id':f'@{ID}',
	'name':name,
	'followers':info[0],
	'following':info[2],
	'posts':info[4]
}

# print informations
for key,value in data.items():
	print(f'{key.capitalize()} : {value}')

input()
