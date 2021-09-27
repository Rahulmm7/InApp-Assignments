import sqlite3
conn=sqlite3.connect(':memory:')
cursor=conn.cursor()
hospital_sql="""
    CREATE TABLE Hospital(
        Hospital_Id INTEGER NOT NULL PRIMARY KEY,
        Hospital_Name TEXT NOT NULL,
        Bed_Count INTEGER NOT NULL)"""
cursor.execute(hospital_sql)

doctor_sql="""
  CREATE TABLE Doctor(
    Doctor_Id INTEGER NOT NULL PRIMARY KEY,
    Doctor_Name TEXT NOT NULL,
    Hospital_Id INTEGER NOT NULL,
    Joining_Date TEXT NOT NULL,
    Speciality TEXT NOT NULL,
    Salary INTEGER NOT NULL,
    Experience INTEGER,
    FOREIGN KEY (Hospital_Id)
    REFERENCES hospital_sql(Hospital_Id))"""
cursor.execute(doctor_sql)

hospitalData = [(1,'Mayo Clinic',200),
                (2,'Cleveland',400),
                (3,'Johns Hopkins',1000),
                (4,'UCLA Medical Center',1500)
                ]

cursor.executemany("INSERT INTO Hospital VALUES(?,?,?)",hospitalData)


doctorData = [
            ('101', 'David', '1', '2005-2-10', 'Pediatric', '40000', 'NULL'),
            ('102', 'Michael', '1', '2018-07-23', 'Oncologist', '20000', 'NULL'),
            ('103', 'Susan', '2', '2016-05-19', 'Garnacologist', '25000', 'NULL'),
            ('104', 'Robert', '2', '2017-12-28', 'Pediatric ', '28000', 'NULL'),
            ('105', 'Linda', '3', '2004-06-04', 'Garnacologist', '42000', 'NULL'),
            ('106', 'William', '3', '2012-09-11', 'Dermatologist', '30000', 'NULL'),
            ('107', 'Richard', '4', '2014-08-21', 'Garnacologist', '32000', 'NULL'),
            ('108', 'Karen', '4', '2011-10-17', 'Radiologist', '30000', 'NULL')
]

cursor.executemany("INSERT INTO Doctor VALUES(?,?,?,?,?,?,?)", doctorData)


d=[]
h=[]
hospital_id=int(input("Enter the Hospital ID"))
print("List of Doctors as per the User entered Hospital ID")
cursor.execute("SELECT Doctor_Name FROM Doctor WHERE Hospital_Id = :id", {"id": hospital_id})
result = cursor.fetchall()
print(result)
i=0
for row in result:
    d.append(row)
    print(row)
result1=cursor.execute("SELECT Hospital_Name FROM Hospital WHERE Hospital_Id = :id", {"id": hospital_id})
for row in result1:
    h.append(row)
    print("{} working in Hospital {}".format(d[i],h[i]))



print("Displaying Hospital Name Using Doctor Name")
name=input("Enter the Doctor Name")
cursor.execute("SELECT * FROM DOCTOR WHERE Doctor_Name = :dname", {"dname": name})
doctor_result=cursor.fetchone()
h_id=doctor_result[2]
cursor.execute("SELECT Hospital_Name FROM HOSPITAL WHERE Hospital_Id = :id", {"id":h_id})
hospital_name = cursor.fetchone()
print("{} working in Hospital {}".format(name,hospital_name ))

conn.commit()
conn.close()
