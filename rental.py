rentals=[]
while True:
    print('''1.register\n 2.view\n 3.update\n 4.delete\n 5.search\n 6.view available \n 7.exit''')
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