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
    