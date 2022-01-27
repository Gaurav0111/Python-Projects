import sqlite3

def connecting():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cal(ID integer PRIMARY KEY , fnumber integer , snumber integer , ans integer)")
    con.commit()
    con.close()

def inserting(fnumber,snumber,result):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(" INSERT INTO cal VALUES(null,?,?,?)",(fnumber,snumber,result))
    con.commit()
    con.close()

def output():
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM cal")
    content = cur.fetchall()
    con.close()
    return content
