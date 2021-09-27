import sqlite3

conn = sqlite3.connect('cars.db')
cursor = conn.cursor()


querry = """ create TABLE Cars(
                                Car_name char(20) NOT NULL,
                                Car_Owner CHAR(20) NOT NULL)"""
cursor.execute(querry)


cursor.execute("insert into Cars values('ford','henry')")
cursor.execute("insert into Cars values('nisaan','majid')")
cursor.execute("insert into Cars values('maruthi','sabu')")
cursor.execute("insert into Cars values('Thar', 'amal')")
cursor.execute("insert into Cars values('BMW','nunu')")
cursor.execute("insert into Cars values('ferrari','enzo')")
cursor.execute("insert into Cars values('KIA','sasi')")
cursor.execute("insert into Cars values('innova','akash')")
cursor.execute("insert into Cars values('cruze','pradeep')")
cursor.execute("insert into Cars values('polo GT','vyshak')")


cursor.execute(" select * from Cars ")
print(cursor.fetchall())
conn.commit()
conn.close()
