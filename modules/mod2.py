#using 1st method
# import mod1
# mod1.fun()
# mod1.fun1()
# print(mod1.a)

#using 2nd method
# from mod1 import fun,fun1,a

# fun()
# fun1()
# print(a)

#using 3rd method
# from mod1 import *
# print(a)
# fun()
# fun1()
# l=input('enter anything: ')
# print(l)

#if we modify import method it will be much easier like this

import mod1 as m
m.fun
m.fun1
m.a