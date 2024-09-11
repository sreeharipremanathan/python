emp=[]
def login():
    uname=input('ener your user name: ')
    passwrd=input('ener your password: ')
    f=0
    if uname=='admin' and passwrd=='admin':
        f=1
    return f

def add_emp():
    id=int(input('enter your id: '))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print('existing id')
            add_emp()
    if f1==0:
        name=(input('enter your name: '))
        age=int(input('enter your age: '))
        salary=int(input('enter your salary: '))
        place=(input('enter your place: '))
        dob=(input('enter your date of birth: '))
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'date_of_birth':dob})
        print('Employee added successfully')
def update():
    id=int(input('enter your id: '))
    f2=0
    for i in emp:
        if i['id']==id:
            f2=1
            name=(input('enter your name: '))
            age=int(input('enter your age: '))
            salary=int(input('enter your salary: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['date_of_birth']=dob
            print('updated successfully')
    if f2==0:
        print('invalid id!!!')
def delete():
    id=int(input('enter your id: '))
    f3=0
    for i in emp:
        if i['id']==id:
            f3=1
            emp.remove(i)
            print('REMOVED!!!')
    if f3==0:
        print('invalid id!!!')
def display():
    print('_'*65)
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','date of birth'))
    print('-'*70)
    for i in emp:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['date_of_birth']))
while True:
    print('''
    1.login
    2.exit''')
    choice=int(input('enter the  choice: '))
    if choice==1:
        f=login()
        if f==1:
            while True:
                print('''
                    1.add emp
                    2.update emp
                    3.delete
                    4.diplay
                    5.logout
                    ''')
                sub_choice=int(input('enter your choice: '))
                if sub_choice==1:
                    add_emp()
                elif sub_choice==2:
                    update()
                elif sub_choice==3:
                    delete()
                elif sub_choice==4:
                    display()
                elif sub_choice==5:
                    break
                else:
                    print('invalid choice')
        elif f==0:
            print('invalid username or passsword!!!')
    elif choice==2:
        break