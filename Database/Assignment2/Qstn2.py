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
                ('Jane',103,32000,222,'trivandrum'),
                ('King',104,40000,223,'Thrissur'),
                ]

cursor.executemany("INSERT INTO Employee VALUES(?,?,?,?,?)",dataEmployee)

cursor.execute("SELECT * FROM Employee")
item = cursor.fetchall()
print("Name \t ID \t Salary \n----- \t --- \t ------")
for i in item:
    print(f"{i[0]}  \t  {i[1]}  \t  {i[2]}")

cursor.execute(""" CREATE TABLE Departments (
                    Department_id INT NOt NULL,
                    Department_name CHAR NOT NULL,
                    FOREIGN KEY (Department_id) REFERENCES Employee(Department_id) ) """)
dataDepartment = [(221,'IT'),
                (221,'Block chain'),
                (222,'AI'),
                (223,'Gaming'),
                (221,'Web Dev'),
                  ]
cursor.executemany("INSERT INTO Departments VALUES (?,?)",dataDepartment)

cursor.execute("SELECT * FROM Departments")
table = cursor.fetchall()
print("Department_id \t Department_name \n------------- \t----------")
for i in table:
    print(f"{i[0]} \t\t\t {i[1]}")

def empDept(id):
    cursor.execute("SELECT * FROM Employee WHERE Department_id = '{}'".format(id))
    details = cursor.fetchall()
    for i in details:
        print(i)



id = int(input("Enetr the Department id of employee to obatin details :"))
empDept(id)

conn.commit()
conn.close()
