
import sqlite3

def connection():
    conn = sqlite3.connect('database.sqlite')
    return conn

def q3a():
    con = connection()
    cursor = con.cursor()
    cursor.execute("""
    SELECT HomeTeam, FTHG , FTAG FROM Matches WHERE hometeam = 'Aachen' and season = '2010' 
     ORDER BY FTHG desc""")
    result  = cursor.fetchall()
    for i in result:
        print(i)

def q3b():
    con = connection()
    cursor = con.cursor()
    cursor.execute(" PRAGMA table_info(Matches)")
    cursor.execute("""
        SELECT  HomeTeam, count(FTR) FROM Matches WHERE  season = '2016' and FTR = 'H' GROUP BY HomeTeam
         ORDER BY count(FTR) desc""")
    result = cursor.fetchall()
    for i in result:
        print(i)
    con.commit()
    con.close()

def q3c():
    con = connection()
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT *  FROM Unique_Teams  ")
    result = cursor.fetchall()
    for i in range(10):
        print(result[i])
    con.commit()
    con.close()
    
def q3d():
    con = connection()
    cursor = con.cursor()
    cursor.execute("""
        SELECT  DISTINCT *    
        FROM Teams_in_Matches INNER JOIN Unique_Teams  
        Where Teams_in_Matches.Unique_Team_ID = Unique_Teams.Unique_Team_ID """)
    result = cursor.fetchall()
    for i in result:
        print(i)
    con.commit()
    con.close()


    
q3a()
q3b()
q3c()
q3d()


