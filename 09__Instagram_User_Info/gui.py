from bs4 import BeautifulSoup
import tkinter,requests,sys,time
from tkinter import *
from PIL import ImageTk,Image

# ! Change the instagram ID here !!!!!!!!!!
ID ='manibarathi_s'

class App:
	def __init__(self):
		
		self.window=tkinter.Tk()
		self.window.geometry('200x300')
		self.window.resizable(0,0)

		self.var1=StringVar()
		self.var2=StringVar()
		self.var3=StringVar()
		self.var=StringVar()

		self.l5=Label(self.window,textvariable=self.var,font='Calibri 11 bold italic',fg='#DF013A')
		self.l2=Label(self.window,textvariable=self.var1,font='Calibri 40 ')
		self.l1=Label(self.window,text="followers",font='Calibri 10 bold',fg='grey')
		self.l3=Label(self.window,textvariable=self.var2,font='Calibri 10 bold',fg='teal',pady=0)
		self.l4=Label(self.window,textvariable=self.var3,font='Calibri 10 bold',fg='teal')
		
		self.set_values()

		self.l5.pack(anchor=CENTER)
		self.l2.pack(anchor=CENTER)
		self.l1.pack(anchor=CENTER)
		self.l3.pack(side=LEFT)
		self.l4.pack(side=RIGHT)
		
		self.window.iconbitmap(r'ig2.ico')
		self.window.mainloop()


	def set_values(self):
		try:
			global ID
			if ID.startswith('@') :
				ID=ID[1:]

			IG=requests.get(f'https://www.instagram.com/{ID}/')
			IG_code=IG.text

			soup=BeautifulSoup(IG_code,'lxml')
			name=soup.title.text.split("(")[0].strip()		#fetching and striping the username

			metatag=soup.find('meta',property='og:description')
			info=(metatag["content"]).replace(',','')
			info=info.split(' ')

			image=soup.find('meta',property="og:image")
			img_url=image["content"]
			profile_pic=requests.get(img_url)

			with open(f'{ID}.jpg','wb') as f:
				f.write(profile_pic.content)
			self.data={
				'id':f'@{ID}',
				'name':name,
				'followers':info[0],
				'following':info[2],
				'posts':info[4]
			} 
			if  not int(self.data['following']) >= 0 or not int(self.data['posts']) >= 0:
				raise TypeError				  
		except Exception as e:
			print(e)
			self.l1.config(text='Something went wrong!\n Unable to fetch proper Data')	
		else:
			#print(self.data)
			self.window.title(f'{self.data["id"]}')
			self.bg_image=ImageTk.PhotoImage(Image.open(f"{ID}.jpg"))
			self.bg_label=Label(self.window,image=self.bg_image)
			self.bg_label.pack(anchor=CENTER)

			self.var.set(self.data['id'])
			self.var1.set(self.data['followers'])
			self.var2.set(f'Following: {self.data["following"]}')
			self.var3.set(f'Posts: {self.data["posts"]}')


App()