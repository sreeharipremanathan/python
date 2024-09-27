# class synnefo:
#     def python():
#         print('python in synnefo')
#     def php():
#         print('php in synnefo')

# std1=synnefo
# std1.python()

# std2=synnefo
# std2.php()


# class bank:
#     def __init__(self,min):
#         self.bal=min
#     def deposite(self,amt):
#         self.bal+=amt
#         print('amount added',self.bal)
#     def withdraw(self,amt):
#         self.bal-=amt
#         print('withdraw successfull...')
#     def dispaly(self):
#         print('balance-->',self.bal)


# user1=bank(0)
# # print(user1.bal)
# user1.deposite(2500)
# print(user1.bal)
# user1.withdraw(1000)
# print(user1.bal)
# user1.dispaly()
# user1.deposite(5000)
# user1.dispaly()

# user2=bank(500)
# user2.deposite(15000)
# user2.dispaly()
# user2.withdraw(5000)
# user2.dispaly()

# user1.deposite(100000)
# user1.dispaly()


# class demo:
#     def __init__(self,name,age):
#         print(name,age)
# obj1=demo('hari',22)


# class demo:
#     def __init__(self,name,age):
#         print(name,age)

# obj=demo(age='22',name='hari')

# class demo:
#     def __init__(self,name,age=22):
#         print(name,age)
# obj1=demo('hari')

# class demo:
#     def __init__(self,*a):
#         print(a)
# obj1=demo('hari',22)

class demo:
    def __init__(self,**a):
        print(a)
obj1=demo(name='hari',age=22)