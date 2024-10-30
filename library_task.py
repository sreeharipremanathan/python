books=[{'id': 11, 'name': 'aa', 'price': 22, 'stock': 222},{'id': 12, 'name': 'abc', 'price': 232, 'stock': 32},{'id': 13, 'name': 'acba', 'price': 44, 'stock': 32}]

def add():
    id=int(input('enter the id: '))
    book_name=input('eneter the name of the book: ')
    price=int(input('enter the price: '))
    stock=int(input('enter the stock: '))
    books.append({'id':id,'name':book_name,'price':price,'stock':stock})

def update():
    id=int(input('enter the id of the book: '))
    f=0
    for i in books:
        if i['id']==id:
            f=1
            price=int(input('enter the updated price: '))
            stock=int(input('enter the updated stock: '))
            i['price']=price
            i['stock']=stock
            print('updated!!!!')
    if f==0:
        print('invalid id!!!')

def remove():
    id=int(input('enetr the id of the book to delete: '))
    for i in books:
        if i['id']==id:
            books.remove(i)
            print('deleted!!!')

def view():
    print('_'*40)
    print("{:<10}{:<15}{:<10}{:<10}".format('id','name','price','stock'))
    print('-'*40)
    for i in books:
        print("{:<10}{:<15}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

def search():
    id=int(input('enter the book id to search: '))
    for i in books:
        if i['id']==id:
            print('_'*40)
            print("{:<10}{:<15}{:<10}{:<10}".format('id','name','price','stock'))
            print('-'*40)
            print("{:<10}{:<15}{:<10}{:<10}".format(i['id'],i['name'],i['price'],i['stock']))

while True:
    print('''
        1.add book
        2.update
        3.remove
        4.view all books
        5.search book
        6.exit
''')
    Choice=int(input('select your option: '))
    if Choice==1:
        add()
    elif Choice==2:
        update()
    elif Choice==3:
        remove()
    elif Choice==4:
        view()
    elif Choice==5:
        search()
    elif Choice==6:
        break
    else:
        print('invalid option!!!')