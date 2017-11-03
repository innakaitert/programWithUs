import sqlite3
import csv


def createTable():
    connection = sqlite3.connect("employee.db")

    cursor = connection.cursor()

    cursor.execute(''' CREATE TABLE employees(
        id INTEGER PRIMARY KEY,
        name VARCHAR(256),
        email VARCHAR(256),
        country VARCHAR(256)
        )''')

    cursor.execute(''' CREATE TABLE phones(
        id INTEGER PRIMARY KEY,
        phone_number VARCHAR(256),
        phone_type VARCHAR(256),
        employees_id INTEGER,
        FOREIGN KEY(employees_id) REFERENCES employees(id) 
        )
        ''')

    connection.commit()

    connection.close()

# createTable() # run it one before moving forward



#  this will let us manipulate out datebase. this was after we made while loop
connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

with open('employees.csv', newline='') as csvfile:
    csvlines = csv.reader(csvfile)
    # for row in csvlines:
    #     print(row)
    #     print(row[0])

# it will insert 
    for row in csvlines:
        cursor.execute(" INSERT INTO employees (name, email, country) VALUES (?,?,?)", (row[0],row[4],row[5]))
        #  attribute that we use as the foreingh key. it automatically ganarate the id
        employees_last_id = cursor.lastrowid
        # this line will work 3 times for every type of phones
        cursor.execute(" INSERT INTO phones (phone_number, phone_type, employees_id) VALUES (?,?,?)", (row[1],"cellphone",employees_last_id))
        cursor.execute(" INSERT INTO phones (phone_number, phone_type, employees_id) VALUES (?,?,?)", (row[2],"homephone",employees_last_id))
        cursor.execute(" INSERT INTO phones (phone_number, phone_type, employees_id) VALUES (?,?,?)", (row[3],"workphone",employees_last_id))


        connection.commit()

connection.close()











