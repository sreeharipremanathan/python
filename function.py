# def function():
#     print('hey')
#     print('welcome')
#     print('to our')
#     print('class')

# function()
# print(10+12)
# function()
# print(10-2)
# function()
# print(10*2)

# def fun1():
#     a=10     #local var
#     print('inside a->',a)
#     print('b=',b)

# b=25    #global var
# fun1()
# print('outside b->',b)

# def fun():
#     global a
#     a=10
#     print(b)

# b=25
# fun()
# print(a,b)

# def function1():
#     return 'welcom',35

# a,b=function1()
# print(a)
# print(b)

def fun2():
    a=10
    b=22
    c=34
    return a,b,c
a1,b1,c1=fun2()
print(a1)
print(b1)
print(c1)