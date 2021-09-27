import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

querry = """ CREATE TABLE Cars(
                                Car_name char(20) NOT NULL,
                                Car_Owner CHAR(20) NOT NULL)"""
cursor.execute(querry)

manyCars = [
            ('ford','henry'),
            ('nisaan','majid'),
            ('maruthi','sabu'),
            ('Thar','amal'),
            ('BMW','henry'),
            ('ferrari','nunu'),
            ('KIA','akash'),
            ('innova','sasi'),
            ('cruze','pradeep'),
            ('polo GT','vyshak')
                        ]

cursor.executemany("INSERT INTO Cars VALUES (?,?) ",manyCars)

cursor.execute(" select * from Cars ")
print(cursor.fetchall())
conn.commit()
conn.close()
