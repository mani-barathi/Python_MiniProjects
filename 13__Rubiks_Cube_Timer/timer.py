import tkinter,time,os,random,threading
from tkinter import *
import tkinter.messagebox

timed = list()
flag = 0
solves = 0
file="times.txt" 

# press spacebar to start and stop timer
# all the times aling with the scrambles will be saved in a text file
# press r to reset the session

def generate_scramble():
	let=["R","R'","L","L'","U","U'","D","D'","F","F'","B","B'","R2","L2","U2","F2","D2","B2"]
	r,l,f,b,u,d=[["R","R'","R2"],["L","L'","L2"],["F","F'","F2"],["B","B'","B2"],["U","U'","U2"],["D","D'","D2"]]
	scramble=""
	prev=str(random.choice(let))
	curr=""
	prevlist=[]
	for i in range(1,22):
		k=0
		while(k==0):
			if(prev in r):
				prevlist=r.copy()
			elif(prev in l):
				prevlist=l.copy()
			elif(prev in f):
				prevlist=f.copy()
			elif(prev in b):
				prevlist=b.copy()
			elif(prev in u):
				prevlist=u.copy()
			elif(prev in d):
				prevlist=d.copy()
			
			curr=str(random.choice(let))
			if(curr in prevlist):
				continue
			else:
				scramble=scramble +" "+curr
				prev=curr
				k=1
	var2.set(scramble)

def display_times(solves):
	listbox.insert(0,var.get())  # 0-start | END -end (position,data)

def save_times():
	global file
	with open(file,"a") as f:  
		f.write(str(var.get())+"  -  "+var2.get()+"\n")     # time - scramble
	

def stats(solves):
	global timed
	var5.set("Best: "+str(min(timed)))
	if(solves>=5):                     #average of 5 
		sol=timed[-5:]
		three=list()
		for j in range(0,5):
			if(sol[j]==min(sol) or sol[j]==max(sol)):
				continue
			else:
				three.append(sol[j])
		su=sum(three)
		avg= '%.2f'%(su/3)
		var4.set("Avg 5: "+avg)

	if(solves>=12):                 #average of 12
		sol=timed[-12:]
		three=list()
		for j in range(0,12):
			if(sol[j]==min(sol) or sol[j]==max(sol)):
				continue
			else:
				three.append(sol[j])
		su=sum(three)
		avg= '%.2f'%(su/10)
		var6.set("Avg 12: "+avg)
		   
def runnging_time():
	global flag
	var2.set("")
	var4.set("")
	var5.set("")
	var6.set("")
	listbox.config(fg="White")
	t=0
	while(flag==1):
		   var.set(t)
		   time.sleep(1)
		   t+=1 
	listbox.config(fg="Black")

def start(event):
	global flag,start_time,end_time,timed,solves,current_scramble
	if(flag==0):
		flag=1
		solves+=1
		start_time=time.time()
		t1=threading.Thread(target=runnging_time)
		t1.start()
		current_scramble=var2.get()
		
	elif(flag==1):
		flag=0
		var2.set(current_scramble)
		var4.set("Avg 5: ")
		var6.set("Avg 12: ")
		end_time=time.time()
		t = "%.2f" % (end_time - start_time)
		clock.config(fg='Black')
		var.set(t)
		tt=float(t)
		timed.append(tt)       #saving times to a list
		display_times(solves)  # displaying to the list
		save_times()           # to the txt file
		generate_scramble()    #generate next scramble
		stats(solves)          # displaying stats

def start_01(event):
	clock.config(fg='Green')

def reset(event):
	timed = list()
	var4.set("Avg 5: ")
	var6.set("Avg 12: ")
	var5.set("Best: ")
	var.set("0.00")
	generate_scramble()
	listbox.delete(0,END)
	solves = 0
# design-----------------------------------------------------------------------------------------------------------
window=tkinter.Tk(className="Cube Timer")

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
# calculate position x, y to get window in center of the screen
w,h=530,450
x = (ws/2) - (w/2)    
y = (hs/2.2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(0,0)
window.iconbitmap(r"download2.ico")

#scrollbar and listbox
scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(window,font="Calibri 12 ",bg="#F0F0ED",width=5,relief=FLAT,highlightthickness=0,selectbackground="#F0F0ED",selectforeground="Black",activestyle=NONE)
#listbox.pack(side = LEFT, fill = Y,pady=20,padx=1) #y represents vertically 
listbox.place(x=2,y=30,height=400)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# scrambnle label
var2=StringVar()
l2=Label(window,font="Ubuntu 12 bold",textvariable=var2)
l2.pack(anchor="center")
generate_scramble()

# Timer label
var=StringVar()
clock=Label(window, font="Roboto 60",textvariable=var)
clock.pack(anchor="center",pady=100)
var.set("0.00")

# avg 5 label
var4=StringVar()
l4=Label(window,font="calibri 14 ",textvariable=var4).place(x=220,y=300)
var4.set("Avg 5: ")

#avg 12 label
var6=StringVar()
l6=Label(window,font="calibri 14 ",textvariable=var6).place(x=220,y=325)
var6.set("Avg 12: ")

# best label
var5=StringVar()
l5=Label(window,font="calibri 14 ",textvariable=var5).place(x=220,y=350)
var5.set("Best: ")

window.bind("<KeyPress-space>",start_01)
window.bind("<KeyRelease-space>",start)
window.bind("<r>",reset)
window.mainloop()