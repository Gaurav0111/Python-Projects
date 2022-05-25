import sqlite3

def connecting():
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items(ID integer PRIMARY KEY, Product text , Price integer , Discount integer)")
    conection.commit()
    conection.close()

def inserting(product,price,discount):
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute(" INSERT INTO items VALUES(null,?,?,?)",(product,price,discount))
    conection.commit()
    conection.close()

def printing():
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("SELECT * FROM items")
    content = cur.fetchall()
    conection.close()
    return content

def searching(product = "" , id = ""):
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("SELECT * FROM items WHERE Product = ? OR id=? ",(product,id))
    content = cur.fetchall()
    conection.close()
    return content

def deleting(id):
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("DELETE FROM items WHERE ID=? " ,(id,))
    conection.commit()
    conection.close()




# ************************************___TABLE__2__***************************************************


def connect():
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS list(ID integer PRIMARY KEY, Product text , Price integer , Discount integer,Quantity integer )")
    conection.commit()
    conection.close()


def insert(product,price,discount,quantity):
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute(" INSERT INTO list VALUES(null,?,?,?,?)",(product,price,discount,quantity))
    conection.commit()
    conection.close()

def printed():
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("SELECT * FROM list")
    content = cur.fetchall()
    conection.close()
    return content

def delete(id):
    con = sqlite3.connect("general_store.db")
    cur = con.cursor()
    cur.execute("DELETE FROM list WHERE ID=? " ,(id,))
    con.commit()
    con.close()

def truncate():
    conection = sqlite3.connect("general_store.db")
    cur = conection.cursor()
    cur.execute("DROP TABLE list")
    connect()
    conection.commit()
    conection.close()

#____________________________________________________- Table 3________________________________________________________



# def create():
#     conection = sqlite3.connect("general_store.db")
#     cur = conection.cursor()
#     cur.execute("CREATE TABLE IF NOT EXISTS history(ID integer PRIMARY KEY, Product text , Price integer , Discount integer,Quantity integer )")
#     conection.commit()
#     conection.close()


# def into(product,price,discount,quantity):
#     conection = sqlite3.connect("general_store.db")
#     cur = conection.cursor()
#     cur.execute(" INSERT INTO history VALUES(null,?,?,?,?)",(product,price,discount,quantity))
#     conection.commit()
#     conection.close()

# def prints():
#     conection = sqlite3.connect("general_store.db")
#     cur = conection.cursor()
#     cur.execute("SELECT * FROM history")
#     content = cur.fetchall()
#     conection.close()
#     return content

# def deletes(id):
#     con = sqlite3.connect("general_store.db")
#     cur = con.cursor()
#     cur.execute("DELETE FROM history WHERE ID=? " ,(id,))
#     con.commit()
#     con.close()




# truncate()
# print(printing())

# print(printing())

# delete(12)
# connect()
# insert(12,"suji",30,0)
# print(printed())

# connect()
# connecting()
# 
# de()

# def updaitng(id,title,author,year,book):
#     con = sqlite3.connect("list_of_books.db")
#     cur = con.cursor()
#     cur.execute("UPDATE books SET title=?,author=?,year=?,book=? WHERE id=?",(title,author,year,book,id))
#     con.commit()
#     con.close()
# connecting()
# inserting("Biscuit",20,0)
# inserting("Toffee",100,0)
# inserting("coffee",200,25)
# inserting("Sugar",40,0)
# inserting("Rice",500,50)

# print(list(printing))
# deleting(1)
# print(printing)