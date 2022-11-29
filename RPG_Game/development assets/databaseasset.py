import sqlite3

def a():
    con = sqlite3.connect("RPG_Game\Data.db")
    c = con.cursor()
    '''c.execute("""CREATE TABLE Inventory(
            Item text,
            Level integer,
            Digits integer
)""")'''
    '''c.execute("INSERT INTO Inventory VALUES ('Sword',1,0)")
    c.execute("INSERT INTO Inventory VALUES ('Sword',2,0)")
    c.execute("INSERT INTO Inventory VALUES ('Sword',3,0)")
    c.execute("INSERT INTO Inventory VALUES ('Spear',1,0)")
    c.execute("INSERT INTO Inventory VALUES ('Spear',2,0)")
    c.execute("INSERT INTO Inventory VALUES ('Spear',3,0)")
    c.execute("INSERT INTO Inventory VALUES ('Armor',1,0)")
    c.execute("INSERT INTO Inventory VALUES ('Armor',2,0)")
    c.execute("INSERT INTO Inventory VALUES ('Armor',3,0)")'''
    c.execute("""UPDATE Inventory SET Digits=1
              WHERE Item='Sword' AND Level=3""")
    c.execute("SELECT Digits FROM Inventory WHERE Item='Sword'AND Level=3")
    print(c.fetchall())
    con.commit()
    con.close