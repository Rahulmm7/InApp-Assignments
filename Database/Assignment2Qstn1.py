import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE Employee(
                    Name CHAR NOT NULL,
                    ID INT PRIMARY KEY,
                    salary INT NOT NULL,
                    Department_id INT NOT NULL)""")

cursor.execute(" ALTER TABLE Employee ADD COLUMN city CHAR ")

dataEmployee = [('John',101,30000,221,'Thrissur'),
                ('Tim',102,35000,221,'kochi'),
                ('Jane',103,32000,221,'trivandrum'),
                ('King',104,40000,221,'Thrissur'),
                ]

cursor.executemany("INSERT INTO Employee VALUES(?,?,?,?,?)",dataEmployee)

cursor.execute("SELECT * FROM Employee")
item = cursor.fetchall()
print("Name \t ID \t Salary \n----- \t --- \t ------")
for i in item:
    print(f"{i[0]}  \t  {i[1]}  \t  {i[2]}")

def readName(letter):
    cursor.execute("SELECT * FROM Employee WHERE Name LIKE '{}%' ".format(letter))
    details = cursor.fetchall()
    for i in details:
        print(i)

def readId(id):
    cursor.execute("SELECT * FROM Employee WHERE ID = {}".format(id))
    details = cursor.fetchall()
    for i in details:
        print(i)

def changeName(id1):
    name = input("Enter the new name :")
    cursor.execute("UPDATE Employee SET Name = '{0}' WHERE ID = {1}".format(name,id1))
    conn.commit()
    cursor.execute("SELECT * FROM Employee WHERE ID = {}".format(id1))
    details = cursor.fetchone()
    print(details)

letter = input("Enetr the ist letter of employee to obtain their details :")
readName(letter)

id = int(input("Enter the id of employee to view details :"))
readId(id)

id1 = int(input("Enter the id of employee whose name want to be changed :"))
changeName(id1)

conn.commit()
conn.close()
