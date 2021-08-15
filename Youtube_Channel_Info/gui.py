import tkinter,requests,threading,time				# pip install requests
from tkinter import *
from googleapiclient.discovery import build			# pip install google-api-python-client
from PIL import ImageTk,Image 						# pip install Pillow

#Youtube API key
# please generate you own youtube API key and replace here
KEY=''
# !!! ID OF YOUTUBE CHANNEL !!!!
ID=''

# press Ctrl + r to refersh so that any program will fetch and replace the data

class App:
	def __init__(self):
		self.window=Tk()
		self.ws = self.window.winfo_screenwidth()
		self.hs = self.window.winfo_screenheight()

		# calculate position x, y
		w,h=250,350
		x = (self.ws) - w -(1/100)*self.ws   
		y = (3/100)*self.hs
		self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
		self.window.config(bg='White')
		self.window.resizable(0,0)
		
		self.namevar=StringVar()
		self.var=StringVar()
		self.var2=StringVar()
		self.var3=StringVar()

		self.namelabel=Label(self.window,textvariable=self.namevar,font='Calibri 16 bold italic',bg='White')
		self.profile_img=Label(self.window)
		self.subscriber=Label(self.window,textvariable=self.var,font='Calibri 35  italic',fg='#FF0040',bg='White')
		self.l2=Label(self.window,text='subscribers',font='Calibri 12 ',fg='#515A5A',bg='White')
		self.videos=Label(self.window,textvariable=self.var2,font='Calibri 20 italic',fg='Teal',bg='White')
		self.l3=Label(self.window,text='videos',font='Calibri 12 ',fg='#515A5A',bg='White')
		self.view=Label(self.window,textvariable=self.var3,font='Calibri 20 italic',fg='#01A9DB',bg='White')
		self.l4=Label(self.window,text='views',font='Calibri 12 ',fg='#515A5A',bg='White')

		self.fetch_set_data()
		
		self.namelabel.pack(anchor=CENTER)
		self.profile_img.pack(anchor=CENTER)
		self.subscriber.pack(anchor=CENTER)
		self.l2.pack(anchor=CENTER)
		self.videos.pack(anchor=CENTER)
		self.l3.pack(anchor=CENTER)
		self.view.pack(anchor=CENTER)
		self.l4.pack(anchor=CENTER)
		
		
		self.window.bind('<Control-r>',self.fetch_set_data)
		self.window.iconbitmap("ytlogo_1.ico")
		self.window.mainloop()


	def fetch_set_data(self,Event=None):
		print('fetched')
		youtube=build('youtube','v3',developerKey=KEY)
		request=youtube.channels().list(part='statistics,snippet',id=ID)
		response=request.execute()
		
		self.profile_name=response['items'][0]['snippet']['title']
		self.profile_img_url=response['items'][0]['snippet']['thumbnails']['medium']['url']
		self.data=response['items'][0]['statistics']

		self.get_image()
		self.image=ImageTk.PhotoImage(Image.open(self.imgname).resize((80, 80), Image.ANTIALIAS))

		self.window.title(self.profile_name)
		self.namevar.set(self.profile_name)
		self.profile_img.config(image=self.image)

		self.var.set(self.data['subscriberCount'])
		self.var2.set(self.data['videoCount'])
		self.var3.set(self.data['viewCount'])

	def get_image(self):
		request=requests.get(self.profile_img_url)
		self.imgname=f'{ID}.jpg'
		with open(self.imgname,'wb') as img:
			img.write(request.content)


if __name__ == '__main__':
	App()
