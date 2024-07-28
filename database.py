import pymysql
import database
from tkinter import messagebox

def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='karthi')
        mycursor = conn.cursor()
    except:
        messagebox.showerror(title='Error', message='Connection is not Established')
        return

    try:
        mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_details')
        mycursor.execute('USE employee_details')
        query = '''
            CREATE TABLE IF NOT EXISTS employee_data(
                Id VARCHAR(30) NOT NULL,
                Name VARCHAR(50),
                Phone VARCHAR(20),
                Role VARCHAR(50),
                Gender VARCHAR(15),
                Salary DECIMAL(10, 2),
                PRIMARY KEY(Id)
            )
        '''
        mycursor.execute(query)
        print('Done with the Connections')
    except Exception as e:
        messagebox.showerror(title='Error', message=str(e))
        mycursor.execute('USE employee_details')


def datachecking(id):
    query = 'SELECT * FROM employee_data WHERE Id = %s'
    mycursor.execute(query, (id,))
    record = mycursor.fetchone()
    if record:
        messagebox.showerror(title='Error', message='User Id already exists')
        return False
    else:
        print("User Name not Exist")
        return True


def insert(id, name, phone, role, gender, salary):
    query = 'INSERT INTO employee_data(Id, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)'
    mycursor.execute(query, (id, name, phone, role, gender, salary))
    conn.commit()
    print('Inserted Sucessfully')

def fetch_employees():
    connect_database()
    mycursor.execute(query='select * from employee_data')
    records = mycursor.fetchall()
    return records


def update(id, name, phone, role, gender, salary):
    mycursor.execute(query='update employee_data set Name = %s, Phone = %s, Role = %s, Gender = %s, Salary = %s where Id = %s', args = (name, phone, role, gender, salary, id))
    conn.commit()
    print('Updates Commited Sucessfully')

def delete_(id):
    mycursor.execute(query='delete from employee_data where Id = %s', args=(id,))
    conn.commit()
    print("Record Deleted Sucessfully")

def deleteall():
    mycursor.execute(query='truncate table employee_data')
    conn.commit()
    print("Deleted all the Records Sucessfully")

def search(field, value):
    query= f'select * from employee_data where {field} LIKE %s'
    mycursor.execute(query, (f"%{value}%",))
    records = mycursor.fetchall()
    return records