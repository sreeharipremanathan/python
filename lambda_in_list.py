# l=[1,2,3,4,5,6,7,8]

# print(list(filter(lambda x:x%2!=0,l)))
# def fun(x):
#     return x%2!=0
# print(list(filter(fun,l)))
# # a=filter(lambda x:x%2==0,l)
# # print(list(a))
# print(list(filter(lambda x:x%2==0,l)))

# def fun(x):
#     return x%2==0
# print(list(filter(fun,l)))

# s=['car','bike','truck','cycle']
# print(list(filter(lambda x:'a' in x,s)))

# def fun(x):
#     return 'a' in x
# print(list(filter(fun,s)))


# map
l=[1,2,3,4,5]
# print(list(map(lambda x:x**3,l)))      '''using lambda'''

'''using user defined function'''
def fun(x):                           
    return x**3
print(list(map(fun,l)))