lms=[{'id':102,'name':'hari','place':'tsr','address':'eng','mobile_no':751055,'email_id':'aa','password':'7510','books':[]}]
books=[{'b_id':11,'book_name':'death note','stock':5,'price':10},{'b_id':12,'book_name':'black clover','stock':7,'price':500}]
def register():
    if len(lms)==0:
        id=101
    else:
        id=lms[-1]['id']+1
    email=input('enter your email id: ')
    f=0
    for i in lms:
        if i['email_id']==email:
            f=1
            print('already existing!!!')
            register()
    if f==0:
        name=input('enter your name: ')
        place=input('enter your place: ')
        address=input('enter your address: ')
        mob=int(input('eneter your mobile number: '))
        password=input('set your password: ')
        lms.append({'id':id,'name':name,'place':place,'address':address,'mobile_no':mob,'email_id':email,'password':password,'books':[]})
        print('registration successfull')
def login():
    uname=input('enter your username (email id): ')
    password=input('enter your passsword: ')
    f=0
    if uname=='admin' and password=='admin':
        f=1
    user=''
    for i in lms:
        if uname==i['email_id'] and password==i['password']:
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
    price=int(input('enter the price: '))
    books.append({'b_id':id,'book_name':bname,'stock':stock,'price':price})

def view_books():
    print('_'*40)
    print("{:<10}{:<15}{:<10}{:<10}".format('book_id','book_name','stock','price'))
    print('-'*40)
    for i in books:
        print("{:<10}{:<15}{:<10}{:<10}".format(i['b_id'],i['book_name'],i['stock'],i['price']))

def book_update():
    id=int(input('enter the book id to be updated: '))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            stock=int(input('enter the updated stock: '))
            price=int(input('enter the updated price: '))
            i['stock']=stock
            i['price']=price
            print('updated successfully.....')
    if f==0:
        print('invalid id!!!')
def delete_book():
    id=int(input('enter the book id to be deleted: '))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            books.remove(i)
            print('DELETED!!!')
    if f==0:
        print('invalid id!!!')

def display_users():
    print('_'*80)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','place','address','mobile_no','email id'))
    print('-'*80)
    for i in lms:
        print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['place'],i['address'],i['mobile_no'],i['email_id']))

def view_profile(user):
    print('_'*85)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','place','address','mobile_no','email id'))
    print('-'*85)
    print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(user['id'],user['name'],user['place'],user['address'],user['mobile_no'],user['email_id']))

def take_book(user):
    id=int(input('enter the book id: '))
    f=0
    for i in books:
        if i['b_id']==id:
            f=1
            if i['stock']>0:
                user['books'].append(i['b_id'])
                i['stock']-=1
            else:
                print('out of stock!!!')
    if f==0:
        print('iinvalid id!!!')

def return_book(user):
    id=int(input('enter the book id: '))
    f=0
    for i in books:
        if i['b_id']==id and id in user['books']:
            f=1
            user['books'].remove(id)
            i['stock']+=1
    if f==0:
        print('book not found!!!')

def book_in_hand(user):
    print(user['books'])


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
                    6.exit
''')
                sub_ch=int(input('enter the choice: '))
                if sub_ch==1:
                    add()
                elif sub_ch==2:
                    view_books()
                elif sub_ch==3:
                    book_update()
                elif sub_ch==4:
                    delete_book()
                elif sub_ch==5:
                    display_users()
                elif sub_ch==6:
                    break
                else:
                    print('invalid option')
        elif f==2:
            while True:
                print('''
                    1.view profile
                    2.view books
                    3.take a book
                    4.return book
                    5.book in hand
                    6.exit
    ''')
                user_choice=int(input('enter your choice: '))
                if user_choice==1:
                    view_profile(user)
                elif user_choice==2:
                    view_books()
                elif user_choice==3:
                    take_book(user)
                elif user_choice==4:
                    return_book(user)
                elif user_choice==5:
                    book_in_hand(user)
                elif user_choice==6:
                    break
                else:
                    print('invalid option!!!')
        else:
            print('invalid user name or password')
    elif choice==3:
        break
    else:
        print('invalid option')