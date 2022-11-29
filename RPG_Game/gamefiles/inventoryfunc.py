import sqlite3

def add_inv(Item,Level,Amount):
    Item = str(Item)
    Amount = int(Amount)
    Level = int(Level)
    con = sqlite3.connect("RPG_Game\Inventory.db")
    c = con.cursor()
    c.execute(f"SELECT Amount FROM Inventory WHERE Item='{Item}'AND Level={Level}")
    before = c.fetchone()[0]
    Amount = int(before) + int(Amount)
    c.execute(f"""UPDATE Inventory SET Amount = {Amount} 
              WHERE Item = '{Item} AND Level ={Level}'""")
    c.execute(f"SELECT Amount FROM Inventory WHERE Item='{Item}'AND Level={Level}")
    con.commit()
    con.close

def sub_inv(Item,Level,Amount):
    Item = str(Item)
    Amount = int(Amount)
    Level = int(Level)
    con = sqlite3.connect("RPG_Game\Inventory.db")
    c = con.cursor()
    c.execute(f"SELECT Amount FROM Inventory WHERE Item='{Item}'AND Level={Level}")
    before = c.fetchone()[0]
    Amount = int(before) - int(Amount)
    c.execute(f"""UPDATE Inventory SET Amount = {Amount} 
              WHERE Item = '{Item} AND Level ={Level}'""")
    c.execute(f"SELECT Amount FROM Inventory WHERE Item='{Item}'AND Level={Level}")
    con.commit()
    con.close
    
def get_inv(Item,Level):
    Item = str(Item)
    Level = int(Level)
    con = sqlite3.connect("RPG_Game\Inventory.db")
    c = con.cursor()
    c.execute(f"SELECT Amount FROM Inventory WHERE Item='{Item}'AND Level={Level}")
    result = (c.fetchone()[0])
    con.commit()
    con.close()
    return result