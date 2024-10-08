import sqlite3

con=sqlite3.connect('python/database/joins.db')
try:
    con.execute("create table std(no int,name text,age int)")
except:
    print('table exist')

try:
    con.execute("create table marks(no int,sub text,mark int)")
except:
    print('table exist')

# con.execute("insert into std(no,name,age)values(1,'a',22),(2,'b',20),(3,'c',21)")
# con.execute("insert into std(no,name,age)values(4,'d',22)")
# con.execute("insert into std(no,name,age)values(5,'e',22)")
# con.commit()

# con.execute("insert into marks(no,sub,mark)values(1,'py',62),(2,'php',75),(4,'java',80),(1,'php',72)")
# con.execute("insert into marks(no,sub,mark)values(3,'php',67)")
# con.execute("insert into marks(no,sub,mark)values(6,'php',88)")
# con.commit()


# inner join
# data=con.execute("select std.no,std.name,std.age,marks.no,marks.sub,marks.mark from std inner join marks on std.no=marks.no")
# for i in data:
#     print(i)

# left join
# data=con.execute("select std.no,std.name,std.age,marks.no,marks.sub,marks.mark from std left join marks on std.no=marks.no")
# for i in data:
#     print(i)

# right join
# data=con.execute("select std.no,std.name,std.age,marks.no,marks.sub,marks.mark from std right join marks on std.no=marks.no")
# for i in data:
#     print(i)

# cross join
data=con.execute("select std.no,std.name,std.age,marks.no,marks.sub,marks.mark from std cross join marks")
for i in data:
    print(i)