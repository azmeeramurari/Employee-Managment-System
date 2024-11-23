import pymysql  # type: ignore
from tkinter import messagebox
def connect_to_database():
    global mycursor,conn
    try:
        conn=pymysql.connect(host='localhost',port=3306,user='root',password='murari')
        mycursor=conn.cursor()
        
        conn.commit()
        messagebox.showinfo('Success', 'Database and table setup complete!')
    except:
        messagebox.showerror('Error','Something went wrong.Please open mysql app before running again')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(10),Salary DECIMAL(10,2) )')
    

def insert(id,name,phone,role,gender,salary):
    mycursor.execute("INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s)",(id,name,phone,role,gender,salary))
    conn.commit()
    print(id,name,phone,role)
def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM employee WHERE id = %s',id)
    result=mycursor.fetchone()
    
    return result[0]>0

def fetch_employees():
      mycursor.execute('SELECT * FROM employee')
        
        # Fetch all rows
      result = mycursor.fetchall()
      return result 

# def fetch_employees():
#     mycursor.execute('SELECT * FROM employee')
#     result=mycursor.fetchall()
#     return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE employee SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()
    
def delete(id):
    mycursor.execute('DELETE FROM employee WHERE id = %s',id)
    conn.commit()

def search(option,value):
        mycursor.execute(f'SELECT * FROM employee WHERE {option}=%s', (value,))
        result=mycursor.fetchall()
        return result
    
# def deleteall_records():
#     mycursor.execute('TRUNCATE TABLE employee')
#     conn.commit()

    
connect_to_database()