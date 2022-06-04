import sqlite3


def connecting():
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contacts(ID integer PRIMARY KEY, name text , number integer , extra text)")
    con.commit()
    con.close()


def inserting(name,number,extra=""):
    name = name.capitalize()
    number = "+" +str(91)+" "+ str(number)
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute(f" INSERT INTO  contacts values (null,?,?,?)",(name,number,extra))
    con.commit()
    con.close()


def printing():
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts")
    content = cur.fetchall()
    con.close()
    return content

def search(name):
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM contacts WHERE name = {name}")
    content = cur.fetchall()  
    con.close()
    return content


def searching(name="",number=""):
    name  = name.capitalize()
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM contacts WHERE name=? OR number=? ",(name,number))
    content = cur.fetchall()  
    if content !="" :
        cur.execute(f"SELECT * FROM contacts WHERE name like {name}.% OR number like {number}.% ",)
        raise Exception ("not found")
    content = cur.fetchall()  
    con.close()
    return content


def deleting(id):
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute("DELETE FROM contacts WHERE ID=? " ,(id,))
    con.commit()
    con.close()

def updating(id,name="",number="",extra=""):
    name = name.capitalize()
    extra = extra.capitalize()
    # number = "+" +str(91)+" "+ str(number)
    con = sqlite3.connect("list_of_contacts.db")
    cur = con.cursor()
    cur.execute("UPDATE contacts SET name=?,number=?,extra =? WHERE id=?",( name,number,extra ,id))
    con.commit()
    con.close()
# updating(5,"" , "","bade tau")
# connecting()
# inserting("Gaurav" , 9568265862)
# inserting("papa" , 9808212274 , "hey its my number")
# deleting(1)
# deleting(2)
# deleting(3)
# deleting(4)
# print(printing())
# print(searching("Pa"))