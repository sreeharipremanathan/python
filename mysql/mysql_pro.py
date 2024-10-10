import mysql.connector
con=mysql.connector.connect(host='localhost',user='hari',password='7510',database='datas')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database datas")
try:
    cur.execute("create table std (rol_no int,name text,age int)")
except:
    print('table exist!!!')
# cur.execute("insert into std (rol_no,name,age)values(1,'achu',22)")

# user input
# rol_no=int(innsert iput('enter the roll no: '))
# name=input('enter your name: ')
# age=int(input('enter your age: '))

# cur.execute("into std (rol_no,name,age)values(%s,%s,%s)",(rol_no,name,age))

# update
# name=input('enetr the new name: ')
# new_name=input('enetr the old name: ')
# cur.execute("update std set name=%s where name=%s",(name,new_name))

# delete
# rol_no=int(input('emter the roll no: '))
# cur.execute("delete from std where rol_no=%s",(rol_no,))

# display
cur.execute("select * from std")
data=cur.fetchall()
print("{:<10}{:<10}{:<10}".format('rol_no','name','age'))
for i in data:
    # print(i)
    print("{:<10}{:<10}{:<10}".format(i[0],i[1],i[2]))
    