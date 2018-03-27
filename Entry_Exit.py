from tkinter import*
from time import *
from random import *
import datetime,os
window=Tk()
window.title('Croud Management')
window.geometry('800x480')
window.configure(bg="orange")
pathEntry ='' 
pathExit =''

try:
    file=open(pathEntry,'r')
    file_In=file.read()
    file.close()
    file_In=file_In.split()
except:
    {}
try:
    if not file_In[-1]=='':
        tag1=int(file_In[-1])
except:
    tag1=100
leave=0
i=1
def entry_Window():
    global tag1
    global i
    global leave
    new_Window = Toplevel(window)
    new_Window.title('Entry')
    new_Window.geometry('300x180')
    new_Window.configure(bg="gold")

    label=Label(new_Window,text="Your Id is Displayed Below!!!")
    label.place(x=200,y=30)
    label.pack()
    entry_label = Label(new_Window, text="")
    entry_label.pack()
    entry_label.place(x=120, y=50)
#for changing the color of the wn
    x = randrange(255)
    y = randrange(255)
    z = randrange(255)
    tag=randrange(100,200)
    rgb_color = [x, y, z]
    mycolor = '#%02x%02x%02x' % (x, y, z)    #for set the background of the window

    #to set the tag into the new window
    new_Window.configure(bg=mycolor)
    #entry_label.configure(text="#"+str(tag))
    tag1=tag1+1
    entry_label.configure(text="#" + str(tag1))
    i=i+1
#get the current time and store into the file

    list1 = list((str(datetime.datetime.now())).split())
    s= str(list1[1])
    entry_time=s[:len(s)-10]

    file=open(pathEntry,'a')
    file.write(entry_time)
    file.write(" ")
    file.write(str(tag1))
    file.write('\n')
    file.close()

#storing the tag value into the file with time
def leave_Window():
    global leave
    new_Window = Toplevel(window)
    new_Window.title('Leave')
    new_Window.geometry('800x480')
    new_Window.configure(bg="gold")

    leave_label= Label(new_Window, text="Leave", font=('arial', 12))
    leave_label.pack()
    leave_label.place(x=200, y=50)

    leave= Entry(new_Window)
    leave.pack()
    leave.place(x=280,y=50)

    Btn = Button(new_Window, text="Exit", font=('arial', 13, 'bold'), command=leave_Exit)
    Btn.pack()
    Btn.place(x=250, y=100)

    #get the current time
def leave_Exit():
    global leave
    alreadyList=[]
    try:
        file2 = open(pathExit,'r')
        iii=1
        file2Data = file2.read()
        file2Data = file2Data.split()
        while(iii<len(file2Data)):
            alreadyList.append(file2Data[iii])
            iii+=2
    except:
        {}
    if leave.get() in alreadyList:
        w2=Tk()
        w2.title('Croud Management')
        w2.geometry('350x300')
        w2.configure(bg="red")
        gk = Label(w2, text=leave.get()+" has already been marked as left!", font=('arial',12))
        gk.pack()
        return
    list1 = list((str(datetime.datetime.now())).split())
    s1 =str(list1[1])
    leave_time = s1[:len(s1) - 10]
    file1=open(pathEntry,'r')
    file_Out = file1.readline().split()
    file_Out = str(file_Out[1])

    #file_Out = str(file_Out[1])
#to store the id and time into the leave.txt
    flagLeave=0
    while file_Out:
        if(leave.get()==file_Out):
            file1=open(pathExit,'a')
            file1.write(leave_time)
            file1.write(" ")
            file1.write(file_Out)
            file1.write("\n")
            flagLeave=1
            

        try:
            file_Out = file1.readline().split()
            file_Out = str(file_Out[1])
        except:
            file_Out = False
    if flagLeave:
        w2=Tk()
        w2.title('Croud Management')
        w2.geometry('350x300')
        w2.configure(bg="red")
        gk = Label(w2, text=leave.get()+" left!", font=('arial',20))
        gk.pack()
        
    if not flagLeave:
        w2=Tk()
        w2.title('Croud Management')
        w2.geometry('350x300')
        w2.configure(bg="red")
        
        gk = Label(w2, text="ERROR!!!", font=('arial',20))
        gk.pack()
        gk = Label(w2, text="Please enter a correct ID number!", font=('arial',12))
        gk.pack()


def kk():
    
    global pathEntry
    global pathExit
    if not os.path.exists(Area.get()):
        os.mkdir(Area.get())
    
    pathEntry = Area.get()+"/"+day.get()+"_"+"Entry.txt"
    pathExit = Area.get()+"/"+day.get()+"_"+"Exit.txt"
    new_Window1 = Toplevel(window)
    new_Window1.title('Entry')
    new_Window1.geometry('800x400')
    new_Window1.configure(bg="gold")
    entry_label = Label(new_Window1, text="Please Choose Any Option", font=('arial', 12))
    entry_label.pack()
    entry_label.place(x=280,y=170)

    B1=Button(new_Window1,text="Entry",font=('arial',13,'bold'),command=entry_Window)
    B1.pack()
    B1.place(x=300,y=210)

    B2=Button(new_Window1,text="Leave",font=('arial',13,'bold'),command=leave_Window)
    B2.pack()
    B2.place(x=400,y=210)                                                                                                                                               



Area_label= Label(window, text="Area Name:", font=('arial', 12))
Area_label.pack()
Area_label.place(x=200, y=50)

Area= Entry(window)
Area.pack()
Area.place(x=300,y=50)

day_label= Label(window, text="Day:", font=('arial', 12))
day_label.pack()
day_label.place(x=200, y=90)

day= Entry(window)
day.pack()
day.place(x=300,y=90)


B2=Button(window,text="Done",font=('arial',13,'bold'),command=kk)
window.quit()
B2.pack()
B2.place(x=350,y=120)

window.mainloop()
