from bs4 import BeautifulSoup
import requests

username="manibarathi_s"

# requesting the instagram site 
IG=requests.get(f'https://www.instagram.com/{username}/')
IG_code=IG.text

# passing the instagram page source code to bs4 object
soup=BeautifulSoup(IG_code,'lxml')
# print(soup)

# getting the details of followers,following and posts
metatag = soup.find('meta',property='og:description')
info = metatag["content"]

info = info.replace(',','')
info = info.split(' ')
# print(info)


# creating a dictionary out of all information
data = {
	'username':f'@{username}',
	'followers':info[0],
	'following':info[2],
	'posts':info[4]
}

# print informations
for key,value in data.items():
	print(f'{key.capitalize()} : {value}')
