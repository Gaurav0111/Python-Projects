from tkinter import *
import sys
import os
from datetime import date 
from tkinter import ttk
from tkinter import messagebox
from fpdf import FPDF
import json
# import requests
    


# def upload_to_drive(name):
#     headers = {"Authorization": "Bearer ya29.a0Aa4xrXNdMxYEyKj6sZDDcARaYw13_uybu2oFcDUvIq0uFhmjbC7-TDJQTQhFCquxOr48Any6NUKD5zIAblhq4CIOW50qqtVDLaWOsmBF9UkDLkDDE0XczuSfI1ConLoUnzOR7-Uf-sxqBMXm5R6iKX8N9XA6aCgYKATASARASFQEjDvL9KIy1gVeA7U-gJQKS9EIiPA0163   "}
#     # name = ""
#     # name += r_number_input.get()
#     # name += ".pdf"
#     para = {
#         "name" : name,
#         # "parents": ["parent folder id"]
#     }
#     files = {
#         'data':('metadata',json.dumps(para),'application/json; charset=UTF-8'),
#         'file': open(f"./{name}",'rb')
#     }
#     r = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers=headers,
#         files=files
#     )

def createRemark(pdf):
    pdf.ln(10)
    result = 3
    pdf.set_font("Arial" ,'B',15)
    pdf.text(15,145,txt='Remarks : ')
    
    if result == 1:
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,157,txt='1.  Accepted')
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,163,txt='2.  Suitable with Rebate')
        pdf.text(36,170,txt='3.  Rejected')
        pdf.text(36,177,txt='4.  Suitable with high rebate')
        pdf.text(45,184,txt="with Factory Manager's Approval")
    
    elif result == 2:
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,152,txt='1.  Accepted')
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,159,txt='2.  Suitable with Rebate')
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,166,txt='3.  Rejected')
        pdf.text(36,173,txt='4.  Suitable with high rebate')
        pdf.text(42,180,txt="with Factory Manager's Approval")
    
    elif result == 3:
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,152,txt='1.  Accepted')
        pdf.text(36,159,txt='2.  Suitable with Rebate')
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,166,txt='3.  Rejected')
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,173,txt='4.  Suitable with high rebate')
        pdf.text(42,180,txt="with Factory Manager's Approval")
    
    elif result == 4:
        pdf.set_font("Arial" ,'',15)
        pdf.text(36,152,txt='1.  Accepted')
        pdf.text(36,158,txt='2.  Suitable with Rebate')
        pdf.text(36,165,txt='3.  Rejected')
        pdf.set_font("Arial" ,'B',18)
        pdf.text(35,172,txt='4.  Suitable with high rebate')
        pdf.text(43,180,txt="with Factory Manager's Approval")

def result():
    if button1.get() == 1:
        return "Material_1"
    elif button2.get() == 1:
        return "Material_2"
    elif button3.get() == 1:
        return "Material_3"
    elif button4.get() == 1:
        return "Material_4"
    elif button5.get() == 1:
        return "Material_5"
    elif button6.get() == 1:
        return "Material_6"
    

def Material_1():
    checkbutton2.deselect()
    checkbutton3.deselect()
    checkbutton4.deselect()
    checkbutton5.deselect()
    checkbutton6.deselect()
    result()
    # print(button1.get())
    pass

def Material_2():
    checkbutton1.deselect()
    checkbutton3.deselect()
    checkbutton4.deselect()
    checkbutton5.deselect()
    checkbutton6.deselect()
    result()
    pass

def Material_3():
    checkbutton1.deselect()
    checkbutton2.deselect()
    checkbutton4.deselect()
    checkbutton5.deselect()
    checkbutton6.deselect()
    result()
    pass

def Material_4():
    checkbutton1.deselect()
    checkbutton2.deselect()
    checkbutton3.deselect()
    checkbutton5.deselect()
    checkbutton6.deselect()
    result()
    pass

def Material_5():
    checkbutton1.deselect()
    checkbutton2.deselect()
    checkbutton3.deselect()
    checkbutton4.deselect()
    checkbutton6.deselect()
    result()
    pass

def Material_6():
    checkbutton1.deselect()
    checkbutton2.deselect()
    checkbutton3.deselect()
    checkbutton4.deselect()
    checkbutton5.deselect()
    result()
    pass

def reset_input():
    # material_name_input.delete(0,END)
    r_number_input.delete(0,END)
    moisture_input.delete(0,END)
    fat_input.delete(0,END)
    protein_input.delete(0,END)
    fibre_input.delete(0,END)
    aish_input.delete(0,END)
    silica_input.delete(0,END)
    analysis_input.delete(0,END)
    checkbutton1.deselect()
    checkbutton2.deselect()
    checkbutton3.deselect()
    checkbutton4.deselect()
    checkbutton5.deselect()
    checkbutton6.deselect()

def createtable(pdf,value):
    pdf.ln(30)
    table_cell_width = 21
    table_cell_height = 6
    pdf.set_font("Arial" ,'B',8)
    columns = ["Material" , "Code No. R" , "Moisture" , "Crude Fat" , "Crude Protien","Crude Fibre ","Total Aish","Sand silica","Remark"]
    for col in columns :
        pdf.cell(table_cell_width , table_cell_height,col , align = 'C' , border = 1)
    pdf.ln(table_cell_height)
    table_cell_height = 30
    for val in value:
        pdf.cell(table_cell_width,table_cell_height,val,align = 'C',border = 1)
    pdf.ln(table_cell_height)

def addText(pdf):
    pdf.ln(10)
    pdf.set_font("Arial" ,'',15)
    pdf.text(15,70,txt="To,")
    pdf.text(140,70,txt=f"Date : {str(date.today())} ")
    pdf.text(15,80,txt="Sequence No.....")
    pdf.ln(8)
    
def generatepdf(pdf):
    # pdf.ln(10)
    pdf.set_font("Arial" ,'',30)
    pdf.text(43,25,txt="CATTLE FEED FACTORY")
    pdf.ln(5)
    pdf.set_font("Arial" ,'',20)
    pdf.text(30,34,txt="Kichha By Pass Road , Rudrapur (U.S. Nagar)")
    pdf.ln(5)
    pdf.set_font("Arial" ,'B',20)
    pdf.text(45,43,txt="LABORATORY ANALYSIS REPORT")
    pdf.ln(5)
    pdf.set_font("Arial" ,'',20)
    pdf.text(70,52,txt="(RAW MATERIAL)")
    pdf.ln(23)
    addText(pdf)
    
def executing():
    if (button1.get() == 0 and button2.get() == 0 and button3.get() == 0 and button4.get() == 0 and button5.get() == 0 and button6.get() == 0) :
        messagebox.showerror("Alert"," Please Select Material Name") 
    elif  r_number_input.get() == '':
        messagebox.showerror("Alert"," Please Enter R Number") 
    else:
        if messagebox.askquestion( "Confirmation", "Are You Sure") == "no":
            return
        value = []
        value.append(result())
        value.append(r_number_input.get())
        value.append(moisture_input.get())
        value.append(fat_input.get())
        value.append(protein_input.get())
        value.append(fibre_input.get())
        value.append(aish_input.get())
        value.append(silica_input.get())
        value.append(analysis_input.get())
        for i in range(len(value)):
            if value[i] == '':
                value[i] = "____"
            else:
                t = ""
                t += str(value[i])
                value[i] = t
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial" ,'B',20)
        generatepdf(pdf)
        createtable(pdf,value)
        createRemark(pdf)
        file_name = ""
        file_name += r_number_input.get()
        file_name += ".pdf"
        # pdf.output(f"report\\{file_name}")  
        pdf.output(file_name)  
        # print(file_name)
        messagebox.showinfo("Information" , "Report has been generated")  
        reset_input()
        os.system(file_name)
        # upload_to_drive(file_name)
        


win = Tk()
win.title("LABORATORY ANALYSIS REPORT")
# win.geometry(f"{win.wininfo_screenwidth}x{win.wininfo_screenhei}")
# win.geometry("1500x820")
# win.attributes('-fullscreen',True)
win.state('zoomed')    

lable1 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable1.grid(row=1,column=1,padx=7,pady=10)

lable1 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable1.grid(row=2,column=1,padx=7,pady=10)

# lable2 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable2.grid(row=2,column=2,padx=7,pady=10)

lable3 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable3.grid(row=2,column=3,padx=7,pady=10)

# lable4 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable4.grid(row=2,column=4,padx=7,pady=10)

# lable7 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable7.grid(row=2,column=4,padx=7,pady=10)

cattel_feed_factory = Label(win,text="CATTLE FEED FACTORY",font=("Arial",15,"bold"))#,width=10,height=2)
cattel_feed_factory.grid(row=2,column=5,padx=7,pady=10)

kichha_bypass_road = Label(win,text="Kichha By Pass Road , Rudrapur (U.S. Nagar)",font=("Arial",15,""))#,width=10,height=2)
kichha_bypass_road.grid(row=4,column=5,padx=7,pady=10)

report = Label(win,text="LABORATORY ANALYSIS REPORT",font=("Arial",15,"bold"))#,width=10,height=2)
report.grid(row=6,column=5,padx=7,pady=10)

report = Label(win,text="(RAW MATERIAL)",font=("Arial",15,""))#,width=10,height=2)
report.grid(row=8,column=5,padx=7,pady=10)

lable8 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable8.grid(row=10,column=7,padx=7,pady=10)

# date = dt.datetime.now()
date_text = Label(win,text=f"Date : {str(date.today())} ",font=('arial',13,'bold'))
date_text.grid(row=10,column=9,padx=10,pady=10)

lable9 = Label(win,text="",font=("",15," "),width=10)#,height=2)
lable9.grid(row=12,column=2,padx=7,pady=10)

# lable10 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable10.grid(row=13,column=2,padx=7,pady=10)

# lable11 = Label(win,text="",font=("",15," "),width=10)#,height=2)
# lable11.grid(row=14,column=2,padx=7,pady=10)

# def selectt():
#     button2.deselect()
#     pass

button1 = IntVar()
button2 = IntVar()
button3 = IntVar()
button4 = IntVar()
button5 = IntVar()
button6 = IntVar()

checkbutton1 = Checkbutton(win, text="D.O.R.B",variable=button1,onvalue=1,offvalue=0,height=2,width=30,command=Material_1)
checkbutton1.grid(row=14,column=2)

checkbutton2 = Checkbutton(win , text="RICE POLISH",variable=button2,onvalue=1,offvalue=0,height=2,width=20,command=Material_2)
checkbutton2.grid(row=15,column=2)

checkbutton3 = Checkbutton(win , text="Material_3",variable=button3,onvalue=1,offvalue=0,height=2,width=10,command=Material_3)
checkbutton3.grid(row=16,column=2)

checkbutton4 = Checkbutton(win , text="Material_4",variable=button4,onvalue=1,offvalue=0,height=2,width=10,command=Material_4)
checkbutton4.grid(row=17,column=2)

checkbutton5 = Checkbutton(win , text="Material_5",variable=button5,onvalue=1,offvalue=0,height=2,width=10,command=Material_5)
checkbutton5.grid(row=18,column=2)

checkbutton6 = Checkbutton(win , text="Material_6",variable=button6,onvalue=1,offvalue=0,height=2,width=10,command=Material_6)
checkbutton6.grid(row=19,column=2)

# material_name_lable = Label(win,text="Name of Material : ",font=("Arial",15,""))
# material_name_lable.grid(row=14,column=8)
# material_name_input = Entry(win,width=30)
# material_name_input.grid(row=14,column=9,padx=20,pady=12)

r_number_lable = Label(win,text="R. Number : ",font=("Arial",15,""))
r_number_lable.grid(row=15,column=8)
r_number_input = Entry(win,width=30)
r_number_input.grid(row=15,column=9,padx=20,pady=12)

moisture_lable = Label(win,text="Moisture : ",font=("Arial",15,""))
moisture_lable.grid(row=16,column=8)
moisture_input = Entry(win,width=30)
moisture_input.grid(row=16,column=9,padx=20,pady=12)

fat_lable = Label(win,text="Crude Fat : ",font=("Arial",15,""))
fat_lable.grid(row=17,column=8)
fat_input = Entry(win,width=30)
fat_input.grid(row=17,column=9,padx=20,pady=12)

protein_lable = Label(win,text="Crude Protein : ",font=("Arial",15,""))
protein_lable.grid(row=18,column=8)
protein_input = Entry(win,width=30)
protein_input.grid(row=18,column=9,padx=20,pady=12)

fibre_lable = Label(win,text="Crude Fibre : ",font=("Arial",15,""))
fibre_lable.grid(row=19,column=8)
fibre_input = Entry(win,width=30)
fibre_input.grid(row=19,column=9,padx=20,pady=12)

aish_lable = Label(win,text="Total Aish : ",font=("Arial",15,""))
aish_lable.grid(row=20,column=8)
aish_input = Entry(win,width=30)
aish_input.grid(row=20,column=9,padx=20,pady=12)

silica_lable = Label(win,text="Sand Silica : ",font=("Arial",15,""))
silica_lable.grid(row=21,column=8)
silica_input = Entry(win,width=30)
silica_input.grid(row=21,column=9,padx=20,pady=12)

analysis_lable = Label(win,text="Other Analysis : ",font=("Arial",15,""))
analysis_lable.grid(row=22,column=8)
analysis_input = Entry(win,width=30)
analysis_input.grid(row=22,column=9,padx=20,pady=12)


submit = Button(win,text="Submit",width=7,font=('arial',13,'bold'),command=executing)
submit.grid(row=17,column=5)

# if material_name_input.get() != '' or r_number_input.get() != '' :
#     submit = Button(win,text="Submit",width=15,font=('arial',13,'bold'),command=executing)
#     submit.grid(row=18,column=6)

reset = Button(win,text="Reset",width=7,font=('arial',13,'bold'),command=reset_input)
reset.grid(row=20,column=5)


win.mainloop()