import sqlite3

def add(Valuename,Value):
    Valuename = str(Valuename)
    Value = int(Value)
    con = sqlite3.connect("RPG_Game\Data.db")
    c = con.cursor()
    c.execute("SELECT Digits FROM Stats WHERE Name='{}'".format(Valuename))
    before = c.fetchone()[0]
    Value = int(before) + int(Value)
    c.execute("""UPDATE Stats SET Digits = {} 
              WHERE Name = '{}'""".format(Value,Valuename))
    c.execute("SELECT Digits FROM Stats WHERE Name='{}'".format(Valuename))
    con.commit()
    con.close

def sub(Valuename,Value):
    Valuename = str(Valuename)
    Value = int(Value)
    con = sqlite3.connect("RPG_Game\Data.db")
    c = con.cursor()
    c.execute("SELECT Digits FROM Stats WHERE Name='{}'".format(Valuename))
    before = c.fetchone()[0]
    Value = int(before) - int(Value)
    c.execute("""UPDATE Stats SET Digits = {} 
              WHERE Name = '{}'""".format(Value,Valuename))
    c.execute("SELECT Digits FROM Stats WHERE Name='{}'".format(Valuename))
    con.commit()
    con.close
    
def get(Valuename):
    Valuename = str(Valuename)
    con = sqlite3.connect("RPG_Game\Data.db")
    c = con.cursor()
    c.execute("SELECT Digits FROM Stats WHERE Name='{}'".format(Valuename))
    result = (c.fetchone()[0])
    con.commit()
    con.close()
    return result