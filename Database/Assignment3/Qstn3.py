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

q3a()
