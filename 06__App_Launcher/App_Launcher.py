import os
import tkinter
from tkinter import *
#---------------------------------------------------------------------------------
window=tkinter.Tk(className="App Launcher")
window.geometry('401x401')
window['bg'] = '#D6DBDF'
window.resizable(0,0)


# widgets--------------------------------------------------------------------------
l1=Label(window,text="Welcome \n Choose the application you want to start",background='#D6DBDF')
l1.place(x=90,y=0)

frame=Frame(window,background='#49A',width=380,height=350).place(x=10,y=40)

l2=Label(frame,text="----App List----",background='#49A')
l2.place(x=160,y=45)



# checkButton's
#-----------left pane(x=30)
var1=IntVar()   #var1.get() will return 1 if checkbutton is ticked
cb1=Checkbutton(frame,text='Chrome',variable=var1,background='#49A')
cb1.place(x=30,y=60)
var2=IntVar()
cb2=Checkbutton(frame,text='MusicBee',variable=var2,background='#49A')
cb2.place(x=30,y=100)
var10=IntVar()
cb10=Checkbutton(frame,text='Teams',variable=var10,background='#49A')
cb10.place(x=30,y=140)
var6=IntVar()
cb6=Checkbutton(frame,text='WhatsApp',variable=var6,background='#49A')
cb6.place(x=30,y=180)
var7=IntVar()
cb7=Checkbutton(frame,text='Touch VPN',variable=var7,background='#49A')
cb7.place(x=30,y=220)
var9=IntVar()



#-------Right pane(x=270)
var3=IntVar()
cb3=Checkbutton(frame,text='VS Code',variable=var3,background='#49A')
cb3.place(x=270,y=60)
var4=IntVar()
cb4=Checkbutton(frame,text='NetBeans',variable=var4,background='#49A')
cb4.place(x=270,y=100)
var5=IntVar()
cb5=Checkbutton(frame,text='Mysql',variable=var5,background='#49A')
cb5.place(x=270,y=140)
var8=IntVar()
cb8=Checkbutton(frame,text='RStudio',variable=var8,background='#49A')
cb8.place(x=270,y=180)


#Launch Button Method -----------------------------------------------------------
# os.startfile() will open the particular file
# change the directory and applications as per your requirement
def Launch():
    if(var1.get()==1):
       os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    if(var2.get()==1):
       os.startfile("C:\Program Files (x86)\MusicBee\MusicBee.exe")
    if(var3.get()==1):
       os.startfile(r"C:\Users\Mani\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    if(var4.get()==1):
        os.startfile("C:/Program Files/NetBeans-11.1/netbeans/bin/netbeans.exe")
    if(var5.get()==1):
        os.startfile(r"C:\Users\Mani\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 5.5\MySQL 5.5 Command Line Client.lnk")
    if(var6.get()==1):
        os.startfile(r"C:\Users\Mani\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\WhatsApp\WhatsApp.lnk")
    if(var7.get()==1):
        os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\TouchVPN.lnk")
    if(var8.get()==1):
        os.startfile("C:\Program Files\RStudio/bin/rstudio.exe")
    if(var10.get()==1):
        os.startfile(r"C:\Users\Mani\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams.lnk") 
     #clear selection
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)


#Button------------------------------------------------------------------------------
b1=Button(frame,text='Launch',command=Launch,background='#AEB6BF')
b1.place(x=175,y=330)


# Driver Code-----------------------------------------------------------------------
window.mainloop()  #keeps window running infinite times unless it is closed