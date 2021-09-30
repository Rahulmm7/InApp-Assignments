import sqlite3

def connection():
    conn = sqlite3.connect('database.sqlite')
    return conn

def q2a():
    con = connection()
    cursor = con.cursor()
    cursor.execute("select count(*) FROM Teams ")
    result = cursor.fetchone()
    print(result[0])
    con.commit()
    con.close()

def q2b():
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT season FROM Teams  ")
    result = cursor.fetchall()
    for i in result:
        print(i[0])
    con.commit()
    con.close()

def q2c():
    con = connection()
    cursor = con.cursor()
    cursor.execute(" select MAX(stadiumcapacity), MIN(stadiumcapacity) from Teams  ")
    result = cursor.fetchall()
    print(result)
    con.commit()
    con.close()

def q2d():
    con = connection()
    cursor = con.cursor()
    cursor.execute("pragma Table_info(Teams)")
    #cursor.execute("select OverallMarketValueHome from Teams")
    result = cursor.fetchall()
    print(result)
    con.commit()
    con.close()


def q2e():
    con = connection()
    cursor = con.cursor()
    cursor.execute("pragma Table_info(Matches)")
    cursor.execute("Select AVG(FTHG) FROM Matches Where HomeTeam = 'Man United' ")
    result = cursor.fetchall()
    print(result)
    con.commit()
    con.close()
    
q2a()
q2b()
q2c()
q2d()
q2e()

