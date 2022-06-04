from tkinter import *
import back_end
from tkinter import messagebox

def view_all():
    list1.delete(0,END)
    for i in back_end.printing():
        list1.insert(END,i)

def insert():
    if e_t.get() in back_end.printing() or e_a.get() in back_end.printing() :
        messagebox.showerror(" Error "," Name or number already in use")
    elif int(len(e_a.get())) != 10 :
        messagebox.showerror(" Error "," Please enter appropriate number !! ")
    else :
        back_end.inserting(e_t.get(),e_a.get(),e_y.get())
        # list1.delete(0,END) 
        list1.insert(END,(e_t.get(),e_a.get(),e_y.get()))
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        view_all()

def search():
    pass

def update():
    # def update_fun():
    back_end.updating(t[0],e_t.get(),e_a.get(),e_y.get())
    view_all()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    selected_row()


def delete():
    back_end.deleting(t[0])
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    view_all()

def selected_row(event):
    global t
    index = list1.curselection()[0]
    t = list1.get(index)
    e1.delete(0,END)
    e1.insert(END,t[1])
    e2.delete(0,END)
    e2.insert(END,t[3])
    e3.delete(0,END)
    e3.insert(END,t[2])
    # print(t)



win = Tk()
win.wm_title("Contact Book")
win.geometry("500x280")

l_1 = Label(win,text='Name')
l_1.grid(row=0,column=0)

l_2 = Label(win,text='Extra Info')
l_2.grid(row=1,column=0)

l_3 = Label(win,text='Number')
l_3.grid(row=0,column=2)

# l_4 = Label(win,text='Book Number')
# l_4.grid(row=1,column=2)


e_t = StringVar()
e1 = Entry(win,textvariable=e_t)
e1.grid(row=0,column=1)

e_y = StringVar()
e2 = Entry(win,textvariable=e_y)
e2.grid(row=1,column=1)

e_a = StringVar()
e3 = Entry(win,textvariable=e_a)
e3.grid(row=0,column=3)

# e_i = StringVar()
# e4 = Entry(win,textvariable=e_i)
# e4.grid(row=1,column=3)

list1 = Listbox(win,height=12,width=45)
list1.grid(row=3,column=0,rowspan=6,columnspan=4)
list1.bind('<<ListboxSelect>>',selected_row)

# s_b1 = Scrollbar(win)
# s_b1.grid(rowspan=6,row=2,column=2)

# list1.configure(yscrollcommand=s_b1.set)
# s_b1.configure(command=list1.yview)

# list1.bind('<<ListboxSelect>>',select_row)

b1 = Button(win,text='View All',width=12,command=view_all)
b1.grid(row=2,column=4)

b2 = Button(win,text='Search Contact',width=12)
b2.grid(row=3,column=4)

b3 = Button(win,text='Add contact',width=12,command=insert)
b3.grid(row=4,column=4)

b4 = Button(win,text='Update',width=12,command=update)
b4.grid(row=5,column=4)

b4 = Button(win,text='Delete',width=12,command=delete)
b4.grid(row=6,column=4)

b4 = Button(win,text='Close' ,width=12,command=win.destroy)
b4.grid(row=7,column=4)

win.mainloop()