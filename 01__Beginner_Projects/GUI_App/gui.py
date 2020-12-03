import tkinter as tk
from tkinter import messagebox
def create_window():
	window=tk.Tk()
	window.title('My App')					# name displayed on the topbar of App
	window.geometry('400x500')				# size of the window

	background_img=tk.PhotoImage(file='24-wallpaper.png')	# for background image
	background_label=tk.Label(window,image=background_img)
	background_label.place(x=0,y=0,relwidth=1,relheight=1)

	# frame (used to group elements in the app)
	frame1=tk.Frame(window,bg='#ecf0f1')
	frame1.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.1)

	# name label
	l1=tk.Label(frame1,text='Name : ',bg='#ecf0f1',font='16')
	l1.place(relwidth=0.40,relheight=0.20,rely=0.1,relx=0.05)
	# name entry
	e1=tk.Entry(frame1,font='16')
	e1.place(relx=0.45,rely=0.1,relheight=0.20,relwidth=0.50)	

	# email label
	l2=tk.Label(frame1,text='Email : ',bg='#ecf0f1',font='16')
	l2.place(relwidth=0.40,relheight=0.20,rely=0.35,relx=0.05)
	# email entry
	e2=tk.Entry(frame1,font='16')
	e2.place(relx=0.45,rely=0.35,relheight=0.20,relwidth=0.50)	

	# gender label
	l3=tk.Label(frame1,text='Gender : ',bg='#ecf0f1',font='16')
	l3.place(relwidth=0.40,relheight=0.20,rely=0.6,relx=0.05)
	#Gender radioButtons
	v=tk.StringVar()
	# both the tri-state value and stringvar value are empty by default that why both of the radio buttons get selected by default
	#to overcome this change the tristatevalue of radiobtn to some non empty string eg ( tristatevalue='x')
	r1=tk.Radiobutton(frame1,text='Male',value='male',variable=v, tristatevalue="x")
	r2=tk.Radiobutton(frame1,text='Female',value='female',variable=v, tristatevalue="x")
	r1.place(relx=0.45,rely=0.6,relwidth=0.2,relheight=0.2)
	r2.place(relx=0.75,rely=0.6,relwidth=0.2,relheight=0.2)

	# Submit Button
	b1=tk.Button(frame1,text='Submit',font='Calibri 14 bold',bg='#b2babb',command=lambda : submit_Btn_pressed(e1,e2,v))
	b1.place(relx=0.4,rely=0.85,relwidth=0.3,relheight=0.12)


	# mainloop() method makes sure to keep the window alive all the time
	window.mainloop()

# this function will run when submit btn is pressed 
def submit_Btn_pressed(e1,e2,v):
	name=e1.get()
	email=e2.get()
	gender=v.get()
	print(name ,email ,gender)
	print(gender)
	if name and email and gender!='':
		messagebox.showinfo("Information",f"welcome {name} !\n")
	else:
		messagebox.showinfo("Warning","Enter All Fields \n")
	# reomve all the text from entry and deselect radio button
	v.set('unknown')
	e2.delete(0,tk.END)
	e1.delete(0,tk.END)

	# deslecting can alse be done by using
	# r1.deselect()


create_window()		