def number():
    a=int(input('enter a number: '))
    b=int(input('enter a number: '))
    return a,b
def add():
    a,b=number()
    print(a+b)
def sub():
    a,b=number()
    print(a-b)
def div():
    a,b=number()
    print(a/b)
def multi():
    a,b=number()
    print(a*b)
def mod():
    a,b=number()
    print(a%b)
while True:
    print('''
        1.addition
        2.substraction
        3.division
        4.mulitiplication
        5.modulous
        6.exit''')
    choice=int(input('enter the choice: '))
    if choice==1:
        add()
        # sum=num1+num2
        # print(sum)
    elif choice==2:
        sub()
        # sub=num1-num2
        # print(sub)
    elif choice==3:
        div()
        # div=num1/num2
        # print(div)
    elif choice==4:
        multi()
        # value=num1*num2
        # print(value)
    elif choice==5:
        mod()
        # mod=num1%num2
        # print(mod)
    elif choice==6:
        break
    else:
        print('invalid option')