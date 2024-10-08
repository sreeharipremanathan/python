import sqlite3

connect=sqlite3.connect('python/database/sample.db')

try:
    connect.execute("create table std(roll_no int,name text,age int,mark real)")
except:
    print('table exist')

# connect.execute("insert into std(roll_no,name,age,mark)values(11,'hari',22,78)")
# connect.execute("insert into std(roll_no,name,age,mark)values(10,'athi',18,68),(8,'achu',24,88),(4,'ayu',25,95)")
# connect.commit()

# data=connect.execute("select * from std where name like 'a%' ")
# for i in data:
#     print(i)
# connect.execute("delete from std where name='achu' ")
# connect.commit()

connect.execute("insert into std(roll_no,name,age,mark)values(11,'hari',22,78)")
data=connect.execute("select name,count(name) from std group by name")
for i in data:
    print(i)