from tkinter import *
import test,output,os

universal = []
universal1 = []

days = ['Monday_','Tuesday_','Wednesday_','Thrusday_',
       'Friday_','Saturday_','Sunday_']
def ok():
    test.main(int(threshold.get()),variable.get()+"_")

def combine(aaa):
    for day in days:
        path = aaa+"/"+day+"Entry.txt"
        try:
            file = open(path,'r')
            fileI = file.read()
            file.close()
            fileI = fileI.split()
            universal.append(day)
            for i in fileI:
                universal.append(i)
        except:
            {}
        
    file2 = open(aaa+"/"+"Entry.txt",'w')
    for ii in universal:
        file2.write(ii+"\n")
    file2.close

    for day in days:
        path = aaa+"/"+day+"Exit.txt"
        try:
            file = open(path,'r')
            fileI = file.read()
            file.close()
            fileI = fileI.split()
            universal1.append(day)
            for i in fileI:
                universal1.append(i)
        except:
            {}
        
    file2 = open(aaa+"/"+"Exit.txt",'w')
    for ii in universal1:
        file2.write(ii+"\n")
    file2.close
            
        

def analyse():
    print("Please Wait...")
    combine(Area.get())
    output.main(Area.get())
    print("Thank You for waiting. Your data has been analysed.")

OPTIONS = [
"Monday", "Tuesday", "Wednesday",
"Thrusday","Friday","Saturday","Sunday"
]

master = Tk()
master.geometry('400x300')

Area_label= Label(master, text="Area Name:", font=('arial', 12))
Area_label.pack()
#Area_label.place() 

Area= Entry(master)
Area.pack()
#Area.place()

threshold_label= Label(master, text="Threshold capacity:", font=('arial', 12))
threshold_label.pack()

threshold= Entry(master)
threshold.pack()

button = Button(master, text="Analyse", command=analyse)
button.pack()


long_S= Label(master, text="Check result after Analysis:", font=('arial', 12))
long_S.pack()

variable = StringVar(master)
variable.set('None')

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

button = Button(master, text="Show", command=ok)
button.pack()
mainloop()
