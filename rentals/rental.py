rentals=[]
while True:
    print('''1.register\n 2.view\n 3.update\n 4.remove\n 5.search\n 6.view available \n 7.exit''')
    choice=int(input('enter your choice: '))
    if choice==1:
        bno=int(input('enter the bike code: '))
        name=input("enter bike's name: ")
        rent=int(input('enter rent: '))
        rentals.append([bno,name,rent])
    elif choice==2:
        print('{:<10}{:<10}{:<10}'.format('bike_code','model','rent/day'))
        for i in rentals:
            print('{:<10}{:<15}{:<10}'.format(i[0],i[1],i[2]))
    elif choice==3:
        bno=int(input("enter bike's code to be updated: "))
        f=0
        for i in rentals:
            if i[0]==bno:
                f=1
                while True:
                    print('''1.update rent\n 2.update bike status\n 3.exit''')
                    ch=int(input('choose any option :'))
                    if ch==1:
                        rent=int(input('enter new rent'))
                        i[2]=rent
                    elif ch==2:
                        status=input('update available or not: ')
                        i.append(status)
                    elif ch==3:
                        break
                    else:
                        print('please choose an valid option :')

        if f==0:
            print('invalid code!!!')
    elif choice==4:
        bno=int(input("enter bike's code to be updated: "))
        f=0
        for i in rentals:
            if i[0]==bno:
                rentals.remove(i)
                f=1
        if f==0:
            print('invalid code!!!')
    elif choice==5:
        bno=int(input("enter bike's code to search: "))
        f=0
        for i in rentals:
            if i[0]==bno:
                print(i)
                f=1
        if f==0:
            print('invalid code!!!')
    elif choice==6:
        for i in rentals:
            if i[3]=='available':
                print('{:<10}{:<10}{:<10}{:<15}'.format('bike_code','model','rent/day','status'))
                print('{:<10}{:<10}{:<10}{:<15}'.format(i[0],i[1],i[2],i[3]))
            elif i[3]=='unavailable':
                print('{:<10}{:<10}{:<10}{:<15}'.format('bike_code','model','rent/day','status'))
                print('{:<10}{:<10}{:<10}{:<15}'.format(i[0],i[1],i[2],i[3]))
    elif choice==7:
        break
    else:
        print('invalid option')