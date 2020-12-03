import tkinter as tk
import datetime
from tkinter import *
import random,threading,time

COLOR_CODES=['#E6B0AA','#F5B7B1','#D7BDE2','#D2B4DE','#A9CCE3','#AED6F1','#A3E4D7','#A2D9CE'
			,'#A9DFBF','#ABEBC6','#F9E79F','#FAD7A0','#F5CBA7','#EDBB99','#D5DBDB']
flag=1

def changeTime():
    global flag

    while flag==1 :
        # getting the current Time 
        current_time = datetime.datetime.now()
        current_time = current_time.strftime("%H:%M")		# getting the time in H:M format

        #changing the text color by randomly picking a value from COLOR_CODES list
        color = random.choice(COLOR_CODES)
        label.config(fg=color)

        # setting the text to the label by the use of var because var is pointing to the text of the label
        var.set(current_time)

        # will delay the excution of loop by 1 second
        time.sleep(1)
 
def stop(Event):
    time.sleep(0.1)
    global flag
    flag=0 
    window.quit()   


if __name__ == '__main__':

	window=tk.Tk(className="Screensaver")
	window.attributes('-fullscreen', True)      # full screen
	window.config(cursor='none')        		# hide the cursor

	var=StringVar()		# to change the text of the Label

	# label 
	label=Label(window,font='Calibri 140',fg='#34495E',textvariable=var)
	label.config(bg='#212F3C')

	# anchor = CENTER will but the label to center of the screen
	# fill = BOTH will expand in both in x and y axis to fill the entire screen
	label.pack(anchor=CENTER,fill=BOTH,expand=True)

	# we create an thread and that thread will run the changeTime()
	t1=threading.Thread(target=changeTime)
	t1.start()

	window.bind('<Key>',stop)			# if any Key is pressed in keyboard then execute the stop function
	window.bind('<Motion>',stop)		# if Mouse is moved then execute the stop function
	window.bind('<Button>',stop)		# if Mouse is Clicked then execute the stop function
	
	window.mainloop()
	# mainloop() is the loop which keeps the entire window(app) active, Once the program control goes inside this loop
	# control will not come out until the window is closed. 
	# This is the reason why we are using an another thread to run changeTime() function
						