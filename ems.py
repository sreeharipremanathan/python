emp=[]
while True:
    print('''
        1.Register
        2.View
        3.Update
        4.Delete
        5.Search
        6.Add Task
        7.Exit''')
    choice=int(input('choose an option: '))
    if choice==1:
        id=int(input('Enter the id: '))
        name=input('enter your name: ')
        age=int(input('Enter your age: '))
        poition=input('enter your position: ')
        salary=int(input('Enter your salary: '))
        exp=int(input('Enter your experience: '))
        emp.append([id,name,age,poition,salary,exp])
    elif choice==2:
        print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<5}'.format('id','Name','Age','position','salary','Experience'))
        for i in emp:
            print('{:<5}{:<10}{:<5}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
    elif choice==3:
        id=int(input('enter the id: '))
        f=0
        for i in emp:
            if i[0]==id:
                print('''1.age \n 2.position \n 3.salary \n 4.experience''')
                ch=int(input('choose any option :'))
                if ch==1:
                    age=int(input("enter updated age: "))
                    i[2]=age
                elif ch==2:
                    poition=input('enter updated position: ')
                    i[3]=poition
                elif ch==3:
                    salary=input('enter updated salary: ')
                    i[4]=salary
                elif ch==4:
                    exp=int(input('enter updated experience: '))
                    i[5]=exp
                else:
                    print('please choose an valid option :')
                f=1
        if f==0:
            print('invali id!!!')
    elif choice==4:
        id=int(input('enter the id to be removed: '))
        f=0
        for i in emp:
            if i[0]==id:
                emp.remove(i)
                f=1
        if f==0:
            print('invalid id!!!')
    elif choice==5:
        id=int(input('enter id of employee: '))
        f=0
        for i in emp:
            if i[0]==id:
                print(i)
                f=1
        if f==0:
            print('employee not found')
    elif choice==7:
        break
    else:
        print('invalid option')