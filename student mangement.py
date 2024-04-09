from tkinter import *
root=Tk()
import mysql.connector as con
from tabulate import tabulate
mycon=con.connect(host="localhost",user="root",passwd="12345678",database="guru")
cursor=mycon.cursor()
def insert(a,b,c):
    cursor.execute(f'insert into empl values({a},"{b}",{c})')
    mycon.commit()
def update(b,c,id):
    cursor.execute(f'update empl set name="{b}",salary={c} where id={id}')
    mycon.commit()
def show():
    from tabulate import tabulate
    cursor.execute("select * from empl")
    data=cursor.fetchall()
    # print(tabulate(data))
    data.grid(row=0,column=0,columnspan=4)
def search(x):
    cursor=mycon.cursor()
    cursor.execute(f'select * from empl where id={x}')
    data=cursor.fetchall()
    print(tabulate(data))
def delete(x):
    cursor.execute(f'delete from empl where id={x}')
    mycon.commit()
while True:
    print("1.insert data")
    print("2.update data")
    print("3.show table")
    print("4.search data")
    print("5.delete data")
    print("6.exit")
    ch=int(input("Enter Your Choice(1-6):"))
    if ch==1:
        x=int(input("Enter id"))
        y=str(input("Enter name"))
        z=int(input("Enter salary"))
        insert(x,y,z)
        print("Inserted Successfully")
    elif ch==2:
        x=int(input("Enter id u want to update "))
        y=str(input("Enter name"))
        z=int(input("Enter salary"))
        update(y,z,x)
        print("Updated Successfully")
    elif ch==3:
        show()
    elif ch==4:
        x=int(input("Enter id "))
        search(x)
    elif ch==5:
        x=int(input("Enter id "))
        delete(x)
    elif ch==6:
        break
