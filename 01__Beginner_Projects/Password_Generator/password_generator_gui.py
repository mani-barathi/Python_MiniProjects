import tkinter
import random 
import pyperclip             # copy text to clipboard
from tkinter import *
from tkinter.ttk import *    # Combobox
import tkinter.messagebox
import os
import datetime
#-----------------------------------------------------------------------------------------------
digits="1234567890"
lower="abcdefghijklmnopqrstuvwxyz"
upper=lower.upper()
special="!@#$%&*()+-/"
password=""
everything=digits+lower+upper+special


#design-------------------------------------------------------------------------------------------
window=tkinter.Tk(className="Password Generator")
window.geometry('350x200')
window.resizable(0,0)
frame=Frame(window,width=350,height=200).place(x=0,y=0)

l1=Label(frame,text="Length  ").place(x=10,y=10)
var2=IntVar()
cb1=Combobox(frame,width=17,values=[8,9,10,11,12,13,14,15],state='readonly',textvariable=var2).place(x=75,y=10)
#cb1['values']=(8,9,10,11,12,13,14,15)
var2.set("8")

l2=Label(frame,text="Password").place(x=10,y=40)
var=StringVar()
e1=Entry(frame,textvariable=var,state='readonly').place(x=75,y=40)

l3=Label(frame,text="Bulk Generation",font='bold').place(x=120,y=80)
l4=Label(frame,text="No of Passwords").place(x=40,y=120)
var3=IntVar()
e2=Entry(frame,textvariable=var3).place(x=150,y=120)

# Methods---------------------------------------------------------------------
def gen_pass():
    global password
    temp_p=""
    password=''
    var.set(temp_p)
    r=var2.get()
    # one character from all types:
    temp_p=temp_p + random.choice(digits)
    temp_p=temp_p + random.choice(lower)
    temp_p=temp_p + random.choice(upper)
    temp_p=temp_p + random.choice(special)
    # remaining  characters
    for i in range(0,r-4):
        temp_p=temp_p+random.choice(everything)
    
    list1=list(temp_p)      # conveting to list because random.shuffle(list) only takes list
    random.shuffle(list1)   # list is shuffled to make no pattern is generated
    password=''.join(list1) # join() method provides a flexible way to create strings from iterable objects. 
    return password
    
def generate_password():
    var.set(gen_pass())
    

def copy_pass():
    if(len(password)==0):
        tkinter.messagebox.showwarning("Warning","No password is generated!")
    else:    
        pyperclip.copy(password)  #copy text to your clipboard
        tkinter.messagebox.showinfo("information","Password copied to you clip board")
        var.set("")

def bulk_generate():
    
    try:
        n=int(var3.get())
        fil=""
        dt=datetime.datetime.now()
        if(n>0):
            fil=r"C:\Users\Mani\Documents\Python\Password_generator/bulk/"+str(n)+"_pass_"+dt.strftime("%d-%m_%H-%M")+".txt"
            print(fil)
            f=open(fil,'w')
            for i in range(0,n):
                pas=gen_pass()
                f.write(pas+"\n")
            tkinter.messagebox.showinfo("information",f"file generated and stored at {fil}")
            var3.set("")
        else:
            tkinter.messagebox.showwarning("warning","Number cannot be 0")    
    except:
        tkinter.messagebox.showwarning("warning","Please enter a number ")
        

#Buttons------------------------------------------------------------------------------------
b1=Button(frame,text="Generate",command=generate_password).place(x=220,y=8)
b2=Button(frame,text="Copy",command=copy_pass).place(x=220,y=38)
b3=Button(frame,text="Bulk generate",command=bulk_generate).place(x=120,y=155)

    

#Driver COde
window.mainloop()