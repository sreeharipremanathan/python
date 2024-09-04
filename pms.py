pms=[]
while True:
    print('''
1.add product
2.update product
3.remove product
4.view product
5.search product
6.exit''')
    choice=int(input('enter your choice: '))
    if choice==1:
        name=input('enter product name: ')
        product_id=int(input('enter product id: '))
        price=int(input('enter price'))
        pms.append({'name':name,'product_id':product_id,'price':price})
    elif choice==2:
        name=input('enter product name')
        f=0
        for  i in pms:
            if i['name']==name:
                f=1
                price=int(input('enter the updated price'))
                i['price']=price
        if f==0:
            print('invalid')
    elif choice==3:
        name = input("Enter the product name to Delete: ")
        f=0
        for i in pms:
            if i['name']==name:
                f=1
                pms.remove(i)
        if f==0:
            print('invalid')
    elif choice==4:
        print("{:<10}{:<10}{:<10}".format('name','product_id','price'))
        for i in pms:
            print("{:<10}{:<12}{:<10}".format(i['name'],i['product_id'],i['price']))
    elif choice==5:
        name = input("Enter the product name to Search: ")
        for i in pms:
            if i['name']==name:
                print('{:<10}{:<10}{:<10}'.format('Name', 'product_id', 'price'))
                print('{:<10}{:<12}{:<10}'.format(i['name'], i['product_id'], i['price']))
    elif choice==6:
        break
    else:
        print('invalid option')