from tkinter import *
import math
import b_d

def add():
    ans = int(ef.get())+int(es.get())
    tx.delete("1.0","end")
    tx.insert(END,ans)
    insert()

def sub():
    ans = int(ef.get())-int(es.get())
    tx.delete("1.0","end")
    tx.insert(END,ans)
    insert()

def multi():
    ans = int(ef.get())*int(es.get())
    tx.delete("1.0","end")
    tx.insert(END,ans)
    insert()

def divide():
    ans = int(ef.get())/int(es.get())
    tx.delete("1.0","end")
    tx.insert(END,ans)
    insert()

def power():
    ans = math.pow(int(e1.get()),int(e2.get()))
    tx.delete("1.0","end")
    tx.insert(END,int(ans))
    insert()

def clear():
    if e1:
        e1.delete(0,END)
    if e2:
        e2.delete(0,END)
    if tx:
        tx.delete("1.0","end")
    if list1:
        list1.delete(0,END)

def insert():
    b_d.inserting(ef.get(),e2.get(),tx.get())
    list1.delete(0,END) 
    list1.insert(END,(ef.get(),e2.get(),tx.get()))

def history():
    list1.delete(0,END)
    for i in b_d.output():
        list1.insert(END,i)

win = Tk()
win.wm_title("Calculator")

l1 = Label(win,text='First Number')
l1.grid(row=0,column=0)

l2 = Label(win,text='Second Number')
l2.grid(row=0,column=2)

l3 = Label(win,text='Result')
l3.grid(row=1,column=0)

list1 = Listbox(win,width=35)
list1.grid(row=2,column=0,columnspan=2,rowspan=20)

ef=StringVar()
e1 = Entry(win,textvariable=ef)
e1.grid(row=0,column=1)

es=StringVar()
e2 = Entry(win,textvariable=es)
e2.grid(row=0,column=3)

tx = Text(win,height=1,width=15)
tx.grid(row=1,column=1)

b1 = Button(win,text='+',width=10,command=add )
b1.grid(row=2,column=2)

b2 = Button(win,text='-',width=10,command=sub )
b2.grid(row=2,column=3)

b3 = Button(win,text='X',width=10,command=multi )
b3.grid(row=3,column=2)

b4 = Button(win,text='/',width=10,command=divide )
b4.grid(row=3,column=3)

b5 = Button(win,text='X^Y',width=10,command=power)
b5.grid(row=5,column=2)

b6 = Button(win,text='AC',width=10,command=clear)
b6.grid(row=5,column=3)

b7 = Button(win,text='History',width=10,command=history)
b7.grid(row=6,column=2)

b6 = Button(win,text='Close',width=10,command=win.destroy)
b6.grid(row=6,column=3)



win.mainloop()