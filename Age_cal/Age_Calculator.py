from tkinter import *
from PIL import ImageTk, Image
from datetime import *


def Calculate():
    list1.delete(0,END)
    dob = e_i.get()
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y" )
    try:
        if int(dob[6::])<int(dt[6::]) or int(dob[6::])==int(dt[6::]) :
            yy = int(dt[6::])-int(dob[6::])-1
            if int(dob[3:5:])==int(dt[3:5:]) or int(dob[3:5:])<int(dt[3:5:]):
                mm = int(dt[3:5])-int(dob[3:5])
            if int(dob[3:5:])>int(dt[3:5:]):
                    mm = (12-int(dob[3:5]))+int(dt[3:5])
            if int(dob[0:2:])==int(dt[0:2:]) or int(dob[0:2:])<int(dt[0:2:]):
                        dd = int(dt[0:2:])-int(dob[0:2:])
            if int(dob[0:2:])>int(dt[0:2:]):
                        dd = int(dob[0:2])-int(dt[0:2]) 
            if int(dt[6::])-int(dob[6::])-1<12:
                yy=00
            if int(dob[0:2])>31:
                list1.insert(END,"Please enter a valid input")
            if int(dob[3:5])>12:
                list1.insert(END,"Please enter a valid input")

            result = f"{dd}/{mm}/{yy}"
            list1.insert(END,"Your age is: "+result)
    
        else:
            list1.insert(END,"Please enter a valid input")
    except:
        list1.insert(END,"Please enter a valid input")
          

   

win = Tk()
win.wm_title("Age Calculator")
win.geometry("400x625")

frame = Frame(win, width=200, height=200)
frame.grid(row=1,column=7)
frame.place(anchor='s', relx=0.5, rely=0.5)
img = Image.open("D:\\Python\\projects\\Age_cal\\a_c.png")
resized_image= img.resize((300,300), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_image)
label = Label(frame, image = img)
label.pack()




l_2 = Label(win)
l_2.grid(row = 0 , column=0)

l_2 = Label(win)
l_2.grid(row = 1 , column=0)

l_2 = Label(win)
l_2.grid(row = 2 , column=0)

l_2 = Label(win)
l_2.grid(row = 3 , column=0)

l_2 = Label(win)
l_2.grid(row = 4 , column=0)

l_2 = Label(win)
l_2.grid(row = 5 , column=0)

l_2 = Label(win)
l_2.grid(row = 6 , column=0)

l_2 = Label(win)
l_2.grid(row = 7 , column=0)

l_2 = Label(win)
l_2.grid(row = 8 , column=0)


l_2 = Label(win)
l_2.grid(row = 11 , column=0)

l_2 = Label(win)
l_2.grid(row = 12 , column=0)

l_2 = Label(win)
l_2.grid(row = 13, column=0)

l_2 = Label(win)
l_2.grid(row = 14 , column=0)

l_2 = Label(win)
l_2.grid(row = 15 , column=0)

l_2 = Label(win)
l_2.grid(row = 16 , column=0)

l_2 = Label(win)
l_2.grid(row = 17 , column=0)


l_1 = Label(win,text='Enter Your Date of Birth in the given Format')
l_1.config(font=('Helvetica bold',10))
l_1.grid(row=18,column=0)

l_2 = Label(win,text=" ")
l_2.grid(row = 19 , column=0)

l_2 = Label(win,text="Date",width=20)
l_2.config(font=('Helvetica bold',10))
l_2.grid(row = 20 , column=0)

e_i = StringVar()
e4 = Entry(win,textvariable=e_i)
e4.insert(INSERT, "DD/MM/YYYY")
e4.grid(row=21,column=3)


l_2 = Label(win,text=" ")
l_2.grid(row = 22 , column=0)

b1 = Button(win,text='Calculate',width=12,command=Calculate)
b1.grid(row=23,column=3)

l_2 = Label(win,text=" ")
l_2.grid(row = 24 , column=0)

l_2 = Label(win,text=" ")
l_2.grid(row = 25 , column=0)

list1 = Listbox(win,height=6,width=35)
list1.grid(row=24,column=0,rowspan=3,columnspan=1)

win.mainloop()