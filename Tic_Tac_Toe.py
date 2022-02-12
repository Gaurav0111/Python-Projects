from tkinter import *
from tkinter import messagebox 

def winner():
    if b1['text']=="O" and b2['text']=="O"  and b3["text"]=="O"  or b4['text']=="O" and b5['text']=="O"  and b6["text"]=="O"  or b7['text']=="O" and b8['text']=="O"  and b9["text"]=="O"  or b1['text']=="O" and b4['text']=="O"  and b7["text"]=="O" or b1['text']=="O" and b5['text']=="O"  and b9["text"]=="O" or b2['text']=="O" and b5['text']=="O"  and b8["text"]=="O" or b3['text']=="O" and b6['text']=="O"  and b9["text"]=="O" or b3['text']=="O" and b5['text']=="O"  and b7["text"]=="O" :
        messagebox._show("Winner of The Game","Player 2 is Winner")

    elif b1['text']=="X" and b2['text']=="X"  and b3["text"]=="X"  or b4['text']=="X" and b5['text']=="X"  and b6["text"]=="X"  or b7['text']=="X" and b8['text']=="X"  and b9["text"]=="X"  or b1['text']=="X" and b4['text']=="X"  and b7["text"]=="X" or b1['text']=="X" and b5['text']=="X"  and b9["text"]=="X" or b2['text']=="X" and b5['text']=="X"  and b8["text"]=="X" or b3['text']=="X" and b6['text']=="X"  and b9["text"]=="X" or b3['text']=="X" and b5['text']=="X"  and b7["text"]=="X" :
        messagebox._show("Winner of The Game","Player 1 is Winner")



win = Tk()


b1 = Button(win,text=" " , command=lambda:button(1))
b1.grid(row=0,column=0,ipadx=20,ipady=20)

b2 = Button(win,text=" " , command=lambda:button(2))
b2.grid(row=0,column=1,ipadx=20,ipady=20)

b3 = Button(win,text=" " , command=lambda:button(3))
b3.grid(row=0,column=2,ipadx=20,ipady=20)

b4 = Button(win,text=" " , command=lambda:button(4))
b4.grid(row=1,column=0,ipadx=20,ipady=20)

b5 = Button(win,text=" " , command=lambda:button(5))
b5.grid(row=1,column=1,ipadx=20,ipady=20)

b6 = Button(win,text=" " , command=lambda:button(6))
b6.grid(row=1,column=2,ipadx=20,ipady=20)

b7 = Button(win,text=" " , command=lambda:button(7))
b7.grid(row=2,column=0,ipadx=20,ipady=20)

b8 = Button(win,text=" " , command=lambda:button(8))
b8.grid(row=2,column=1,ipadx=20,ipady=20)

b9 = Button(win,text=" " , command=lambda:button(9))
b9.grid(row=2,column=2,ipadx=20,ipady=20)

player = 1

def button(value):
    global player
    if value == 1 and player == 1 :
        b1.config(text="X")
        player = 2
    elif value == 1 and player == 2 :
        b1.config(text="O")
        player = 1 
    
    elif value == 2 and player == 1 :
        b2.config(text="X")
        player = 2
    elif value == 2 and player == 2 :
        b2.config(text="O")
        player = 1 
    
    
    elif value == 3 and player == 1 :
        b3.config(text="X")
        player = 2
    elif value == 3 and player == 2 :
        b3.config(text="O")
        player = 1 

    
    elif value == 4 and player == 1 :
        b4.config(text="X")
        player = 2
    elif value == 4 and player == 2 :
        b4.config(text="O")
        player = 1 

    
    elif value == 5 and player == 1 :
        b5.config(text="X")
        player = 2
    elif value == 5 and player == 2 :
        b5.config(text="O")
        player = 1 

    
    elif value == 6 and player == 1 :
        b6.config(text="X")
        player = 2
    elif value == 6 and player == 2 :
        b6.config(text="O")
        player = 1 

    
    elif value == 7 and player == 1 :
        b7.config(text="X")
        player = 2
    elif value == 7 and player == 2 :
        b7.config(text="O")
        player = 1 

    
    elif value == 8 and player == 1 :
        b8.config(text="X")
        player = 2
    elif value == 8 and player == 2 :
        b8.config(text="O")
        player = 1 

    elif value == 9 and player == 1 :
        b9.config(text="X")
        player = 2
    elif value == 9 and player == 2 :
        b9.config(text="O")
        player = 1 
    winner()


win.mainloop()