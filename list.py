# l=[11,24,'abc',3.4]
# for i in l:
#     print(i)


# if 10 in l:
#     print("avil")
# else:
#     print("not avil")
# print(l)
# print(l[2])
# updated abc into another value
# l[2]="hari"
# print(l[2])
# l[1]="hey"
# print(l)
# methods to add

# l.append([1,2,3])
# l.append("hey there!")

# l.extend(['hello',"hari",18])

# l.insert(2,"i'm")
# print(l)
# print(l[5][2])  

# methods to delete
# l.clear()
# print(l)

# l.pop()
# print(l)

# l.pop(0)
# print(l)

# l.remove("hello")
# print(l)

# l.insert(-1,'hello')
# print(l)

# l=[7,8,9,5,3,22,1]
# l.sort()
# print(l)
# l.reverse()
# print(l)

# l1=l
# print(id(l))
# print(id(l1))
# print(l)
# print(l1)
# l1.pop()
# print(l)
# print(l1)

# l1=l.copy()
# print(id(l))
# print(id(l1))
# l1.pop()
# print(l)
# print(l1)


# print(l.index(22))

# tsk
# l=[7,8,9,5,2,4,3,22,1]
# sum=0
# for i in l:
#     if i%2==0:
#         print(i)
#         sum+=i
# print("sum of even numbers is= ",sum)

# l=['hello','welcome','hari']
# l.reverse()
# print(l)
# for i in l:
#     print(i[::-1])

# l=[1,2,4.5,'hey']
# sum=0
# for i in l:
#     print(type(i))
#     if type(i)==int or type(i)==float:
#         sum+=i
# print(sum)

# l=[2,4,5,4,2,5,6,7]
# l1=[]
# for i in l:
#     if i not in l1:
#         l1.append(i)
# print(l1)

# names=[]
# limit=int(input("enter the number of names: "))
# for i in range(limit):
#     name=input('enter the name: ')
#     names.append(name)
# print(names)

# names=[]
# limit=int(input("enter the number of names: "))
# for i in range(limit):
#     name=input('enter the name: ')
#     age=int(input('enter the age: '))
#     mark=int(input('enter the mark: '))
#     names.append([name,age,mark])
# print(names)

# student management system
# -------------------------
std=[]
while True:
    print('''
        1.add std
        2.view std
        3.update std
        4.delete std
        5.search
        6.exit''')
    choice=int(input('please choose an option: '))
    if choice==1:
        name=input('enter the name: ')
        age=int(input('enter the age: '))
        mark=int(input('enter the mark: '))
        std.append([name,age,mark])
    elif choice==2:
        print('{:<10}{:<5}{:<5}'.format('name','age','mark'))
        for i in std:
            print('{:<10}{:<5}{:<5}'.format(i[0],i[1],i[2]))
    elif choice==3:
        name=input('enter the name: ')
        f=0
        for i in std:
            if i[0]==name:
                print('''1.update name \n 2.update age \n 3.update mark''')
                ch=int(input('choose the option: '))
                if ch==1:
                    name=input('enter the updated name: ')
                    i[0]=name
                elif ch==2:
                    age=input('enter the updated age: ')
                    i[1]=age
                elif ch==3:
                    mark=int(input('enter the new mark: '))
                    i[2]=mark
                else:
                    print('enter a valid choice')
                f=1
        if f==0:
            print('name is not in the list!!!')
    elif choice==4:
        name=input('enter the name to be deleted: ')
        f=0
        for i in std:
            if i[0]==name:
                std.remove(i)
                f=1
        if f==0:
            print('name is not in list!!!')
    elif choice==5:
        name=input('enter the name: ')
        f=0
        for i in std:
            if i[0]==name:
                print(i)
                f=1
        if f==0:
            print('the name no found!!!')
    elif choice==6:
        break
    else:
        print('invalid option')