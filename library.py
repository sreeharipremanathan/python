lms=[]
books=[]
def register():
    if len(lms)==0:
        id=101
    else:
        id=lms[-1]['id']+1
    email=input('enter your email id: ')
    f=0
    for i in lms:
        if i['mail_id']==email:
            f=1
            print('already existing!!!')
            register()
    if f==0:
        name=input('enter your name: ')
        place=input('enter your place: ')
        address=input('enter your address: ')
        mob=int(input('eneter your mobile number: '))
        password=input('set your password: ')
        lms.append({'id':id,'name':name,'place':place,'address':address,'mobile_no':mob,'mail_id':email,'password':password})
        print('registration successfull')
def login():
    uname=input('enter your username (email id): ')
    password=input('enter your passsword: ')
    f=0
    if uname=='admin' and password=='admin':
        f=1
    user=''
    for i in lms:
        if uname==i['mail_id'] and password==i['password']:
            f=2
            user=i
    return f,user
def add():
    if len(books)==0:
        id=10
    else:
        id=books[-1]['b_id']+1
    bname=input('enter the name of book: ')
    stock=int(input('enter the stock: '))
    price=int(input('enter the price'))
    books.append({'b_id':id,'book_name':bname,'stock':stock,'price':price})

def view_books():
    print('_'*40)
    print("{:<10}{:<15}{:<10}{:<10}".format('book_id','book_name','stock','price'))
    print('-'*40)
    for i in books:
        print("{:<10}{:<15}{:<10}{:<10}".format(i['b_id'],i['book_name'],i['stock'],i['price']))
while True:
    print('''
            1.register
            2.login
            3.exit
''')
    choice=int(input('enter your choice: '))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                    1.add books
                    2.view books
                    3.update books
                    4.delete books
                    5.view users
''')
                sub_ch=int(input('enter the choice'))
                if sub_ch==1:
                    add()
                elif sub_ch==2:
                    view_books()
        elif f==2:
            print('user login')
        else:
            print('invalid user name or password')