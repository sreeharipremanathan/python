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