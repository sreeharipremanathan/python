def number():
    a=int(input('enter a number: '))
    b=int(input('enter a number: '))
    return a,b

add=lambda a,b:a+b
sub=lambda a,b:a-b
div=lambda a,b:a/b
mul=lambda a,b:a*b
mod=lambda a,b:a%b
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
        a,b=number()
        print(add(a,b))
    elif choice==2:
        a,b=number()
        print(sub(a,b))
    elif choice==3:
        a,b=number()
        print(div(a,b))
    elif choice==4:
        a,b=number()
        print(mul(a,b))
    elif choice==5:
        a,b=number()
        print(mod(a,b))
    elif choice==6:
        break
    else:
        print('invalid option')
