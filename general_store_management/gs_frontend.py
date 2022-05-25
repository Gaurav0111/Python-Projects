from tkinter import *
import gs_Backend
from tkinter import ttk
from tkinter import messagebox
import time
import datetime as dt

total_list = []
history = []
def insert():
    if e13.get() == "" or e14.get()=="" or e15.get()=="" or e16.get()=="" :
        messagebox.showerror("Aleart"," Please Enter Product Name and Quantity")
    else:
        gs_Backend.inserting(e13.get(),e15.get(),e16.get())
        e13.delete(0,END)
        e14.delete(0,END)
        e15.delete(0,END)
        e16.delete(0,END)
        
def view_All():
    
    da_te = f"{date:%B,%d}"
    lst_list.delete(0,END)
    lst_list.insert(END , "                                                                                                                                                      ||    XYZ    Shop    Management   Project   ||  ")
    lst_list.insert(END," ")
    # lst_list.insert(END , "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    lst_list.insert(END , "=========================================================================================================================================================================================================")
    lst_list.insert(END," ")
    lst_list.insert(END, "                                        ID                                        Date                                        Product                                        Price                                        Discount/pack                                         ")
    for i in gs_Backend.printing():
        lst_list.insert(END,f"                                        {i[0]}                                        {da_te}                                     {i[1]}                                        {i[2]}                                                  {i[3]}")

def dele():
    product_name = history[0]
    product_details = gs_Backend.searching(product_name)
    # print(product_details[0][0])
    gs_Backend.deleting(product_details[0][0])
    view_All()
    history.clear()
    
def select_row(event):
    b13 = Button(box2,text="Delete",width=10,font=('arial',13,'bold'),command=dele)
    b13.grid(row=10,column=13)
    global t
    index = lst_list.curselection()
    t = lst_list.get(index)
    i = 124
    while True:
        if t[i+1]==" " and t[i+2]==" ":
            break
        else:
            i += 1
    product_name = t[124:i+1]
    history.append(product_name)
    product_details = gs_Backend.searching(product_name)
    e13.delete(0,END)
    e13.insert(END,product_details[0][1])
    e14.delete(0,END)
    e14.insert(END,product_details[0][1])
    e15.delete(0,END)
    e15.insert(END,product_details[0][2])
    e16.delete(0,END)
    e16.insert(END,product_details[0][3])


def add():
    if e3.get() == "" or e4.get()=="":
        messagebox.showerror("Aleart"," Please Enter Product Name and Quantity")
    else:
        product_name = e3.get()
        product_quantity = e4.get()
        # try :
        for _ in range(1):
            lst = gs_Backend.searching(product_name)
            gs_Backend.insert(lst[0][1],lst[0][2],lst[0][3],product_quantity)
            bill.delete(0,END)
            bill.insert(END , "                                                                                                                                                      ||    XYZ    Shop    Management   Project   ||  ")
            bill.insert(END , "___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
            bill.insert(END, "                    ID                    Date                    Product                    Price                    Discount/pack                    Quantity                                                                                                                        || Total ")
            bill.insert(END,"")
            for j in gs_Backend.printed():
                i = list(j)
                da_te = f"{date:%B ,%d}"
                # if e6.get()!="":
                #     i[3]=e6.get()
                Total = (int(i[2])*int(product_quantity))-(int(product_quantity)*int(i[3]))
                total_list.append(Total)
                bill.insert(END,f"                    {i[0]}                    {da_te}                    {i[1]}                         {i[2]}                                     {i[3]}                      {i[4]}                                                                                                                                     ||{Total}")

            
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            # total_list.clear()



        # except Exception as e:
            # messagebox.showerror("Error","opss... Product Not Found ")

def invoice():
    bill.insert(END,"____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
    bill.insert(END, f"                    Total                                                                                                                                                                                                                                                                                        {sum(total_list)}" )
    # total_list.clear()
    

def reset():
    
    bill.delete(0,END)
    gs_Backend.truncate()


win = Tk()
win.wm_title("Invoice Generator")
win.geometry("1500x700")
# win.attributes('-fullscreen',True)

tabs = ttk.Notebook(win)
box1 = ttk.Frame(tabs)
box2 = ttk.Frame(tabs)
box3 = ttk.Frame(tabs)
tabs.add(box1 , text="Selling")
tabs.add(box2 , text="Inserting")
# tabs.add(box3 , text="Deleting")
tabs.pack(expand=1,fill="both")


#*******************************************************TAB_1*******************************************************

# l1 = Label(box1,text="Date",font=(" ",15," "),width=7,height=2)
# l1.grid(row=2,column=3,padx=7,pady=10)
date = dt.datetime.now()
e1 = Label(box1,text=f"{date: %A,%B ,%d,%Y}",font=('arial',13,'bold'))
e1.grid(row=2,column=2,padx=10,pady=10)

# l3 = Label(box1,text=" ",font=(" ",15," "),width=10,height=2)
# l3.grid(row=2,column=11,padx=7,pady=10)

# l2 = Label(box1,text="Time",font=(" ",15," "),width=7,height=2)
# l2.grid(row=2,column=13,padx=7,pady=15)
# ti_me=StringVar()
b4 = Button(box1,text="Reset",font=('arial',13,'bold'), command=reset)
b4.grid(row=2,column=20)


l4 = Label(box1,text="Product",font=(" ",15," "),width=12,height=2)
l4.grid(row=5,column=3,padx=7,pady=10)
prod=StringVar()
e3 = Entry(box1,textvariable=prod)
e3.grid(row=5,column=6,padx=10,pady=10)


# l6 = Label(box1,text=" ",font=(" ",15," "),width=8,height=2)
# l6.grid(row=5,column=9,padx=7,pady=10)

l5 = Label(box1,text="Quatity",font=(" ",15," "),width=5,height=2)
l5.grid(row=5,column=10,padx=7,pady=10)
quantity=StringVar()
e4 = Entry(box1,textvariable=quantity)
e4.grid(row=5,column=11,padx=10,pady=10)


l7 = Label(box1,text="Price",font=(" ",15," "),width=12,height=2)
l7.grid(row=8,column=3,padx=7,pady=10)
price=StringVar()
e5 = Entry(box1,textvariable=price)
e5.grid(row=8,column=6,padx=10,pady=10)


# l9 = Label(box1,text=" ",font=(" ",15," "),width=8,height=2)
# l9.grid(row=8,column=9,padx=7,pady=10)

l8 = Label(box1,text="Discount",font=(" ",15," "),width=10,height=2)
l8.grid(row=8,column=10,padx=7,pady=10)
discount=StringVar()
e6 = Entry(box1,textvariable=discount)
e6.grid(row=8,column=11,padx=10,pady=10)


l10 = Label(box1,text=" ",font=(" ",15," "),width=5,height=1)
l10.grid(row=9,column=8,padx=7,pady=10)

b1 = Button(box1 , text="Generate Invoice",font=('arial',13,'bold'),command=invoice)
b1.grid(row=10,column=8,)

b2 = Button(box1,text="Add",width=7,font=('arial',13,'bold'),command=add)
b2.grid(row=10,column=11)

b3 = Button(box1,text="Delete",width=10,font=('arial',13,'bold'))
b3.grid(row=10,column=13)

l10 = Label(box1,text=" ",width=8,height=1)
l10.grid(row=11,column=8,padx=7,pady=10)

bill = Listbox(box1,width=200,height=22)
bill.grid(row=12,column=2,columnspan=60)



#******************************************************************TAB_2************************************************

date = dt.datetime.now()
e11 = Label(box2,text=f"{date: %A,%B ,%d,%Y}",font=('arial',13,'bold'))
e11.grid(row=2,column=2,padx=10,pady=10)


# l13 = Label(box1,text=" ",font=(" ",15," "),width=10,height=2)
# l13.grid(row=2,column=11,padx=7,pady=10)

# l12 = Label(box1,text="Time",font=(" ",15," "),width=7,height=2)
# l12.grid(row=2,column=13,padx=7,pady=15)
# ti_me=StringVar()
# b14 = Button(box2,text="Reset",font=('arial',13,'bold'), command=reset)
# b14.grid(row=2,column=20)


l14 = Label(box2,text="Product",font=(" ",15," "),width=12,height=2)
l14.grid(row=5,column=3,padx=7,pady=10)
prod=StringVar()
e13 = Entry(box2,textvariable=prod)
e13.grid(row=5,column=6,padx=10,pady=10)


# l16 = Label(box1,text=" ",font=(" ",15," "),width=8,height=2)
# l16.grid(row=5,column=9,padx=7,pady=10)

l15 = Label(box2,text="Quatity",font=(" ",15," "),width=5,height=2)
l15.grid(row=5,column=10,padx=7,pady=10)
quantity=StringVar()
e14 = Entry(box2,textvariable=quantity)
e14.grid(row=5,column=11,padx=10,pady=10)


l17 = Label(box2,text="Price",font=(" ",15," "),width=12,height=2)
l17.grid(row=8,column=3,padx=7,pady=10)
price=StringVar()
e15 = Entry(box2,textvariable=price)
e15.grid(row=8,column=6,padx=10,pady=10)


# l19 = Label(box1,text=" ",font=(" ",15," "),width=8,height=2)
# l19.grid(row=8,column=9,padx=7,pady=10)

l18 = Label(box2,text="Discount",font=(" ",15," "),width=10,height=2)
l18.grid(row=8,column=10,padx=7,pady=10)
discount=StringVar()
e16 = Entry(box2,textvariable=discount)
e16.grid(row=8,column=11,padx=10,pady=10)


l20 = Label(box2,text=" ",font=(" ",15," "),width=5,height=1)
l20.grid(row=9,column=8,padx=7,pady=10)

b11 = Button(box2 , text="Insert",font=('arial',13,'bold'), command=insert)
b11.grid(row=10,column=8,)

b12 = Button(box2,text="View All",width=7,font=('arial',13,'bold'),command=view_All)
b12.grid(row=10,column=11)

# b13 = Button(box2,text="Delete",width=10,font=('arial',13,'bold'))
# b13.grid(row=10,column=13)


l19 = Label(box2,text=" ",width=8,height=1)
l19.grid(row=11,column=8,padx=7,pady=10)

lst_list = Listbox(box2,width=200,height=22)
lst_list.grid(row=12,column=2,columnspan=60)
lst_list.bind('<<ListboxSelect>>',select_row)


win.mainloop()

