import num
import add
from substract import sub
from multi import *
from div import div as d
from mod import *
while True:
    print('''
        1.add
        2.substract
        3.multiplication
        4.division
        5.modulous
        6.exit
''')
    choice=int(input('enter the choice: '))
    if choice==1:
        a,b=num.num()
        add.add(a,b)
    elif choice==2:
        a,b=num.num()
        sub(a,b)
    elif choice==3:
        a,b=num.num()
        multi(a,b)
    elif choice==4:
        a,b=num.num()
        d(a,b)
    elif choice==5:
        a,b=num.num()
        mod(a,b)
    elif choice==6:
        break
    else:
        print('invalid')