# print('exception handling')
# a='welcome'
# b=20
# try:
#     print(a+b)
# except:
#     print("there's an error")
# else:
#     print('work without error')
# finally:
#     print("error or not it'll work")

l=[1,2,3,'abc',4,6.5]
sum=0
for i in l:
    if type(i)==int or type(i)==float:
        sum+=i
    # try:
    #     sum=sum+i
    # except:
    #     pass
print(sum)