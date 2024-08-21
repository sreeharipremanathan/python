# "we can use range in 3 type"
# range(limit)
# for i in range(5):
#     print(i)

# range(start,end)
# for i in range(1,11):
#     print(i)

# range(start,end,updation)
# for i in range(2,21,2):
#     print(i)

# sum of n numbers
# ----------------
# start=int(input('enter the starting value :'))
# end=int(input('enter the ending value :'))
# sum=0
# for i in range(start,end+1):
#     sum+=i
# print(sum)

# print even numbers
# ------------------
# start=int(input('enter the starting value :'))
# end=int(input('enter the ending value :'))
# for i in range(start,end+1):
#     if i%2==0:
#       print(i)

# print odd numbers
# -----------------
# start=int(input('enter the starting value :'))
# end=int(input('enter the ending value :'))
# for i in range(start,end+1):
#     if i%2!=0:
#       print(i)

# sum of n numbers, even and odd numbers
# --------------------------------------
# start=int(input('enter the starting value :'))
# end=int(input('enter the ending value :'))
# even=0
# odd=0
# sum=0
# for i in range(start,end+1):
#     sum+=i
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print('sum of even numbers:',even)
# print('sum of odd numbers:',odd)
# print('sum of n numbers:',sum)

# multiplication table
# ----------------------
# value=int(input('enter the value'))
# product=0
# for i in range(1,10+1):
#     product=value*i
#     print(i,'*',value,'=',product)

# factorial of a number
# --------------------
# num=int(input('enter a number :'))
# fact=1
# for i in range(1,num+1):
#     fact*=i
# print(fact)

# to print letters in a string
# ----------------------------
# string=input('enter a string: ')
# for i in string:
#     print(i)

# to print a string in reverse
# ----------------------------
a=input('enter a string :')
rev=''
for i in a:
    rev=i+rev
print(rev)