a=int(input('enter a numver :'))
b=int(input('enter a numver :'))
c=int(input('enter a numver :'))
if a>b:
    if a>c:
        print('the greatest is',a)
    else:
        print('the greatest is',c)
else:
    if b>c:
        print('the greatest is',b)
    else:
        print('the greatest is',c)