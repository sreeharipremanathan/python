# i=1
# while i<=10:
#     print(i)
#     i+=1

# i=int(input('enter the starting value :'))
# end=int(input('enter the ending value :'))
# while i<=end:
#     print(i)
#     i+=2

# i=1
# end=int(input('enter the limit :'))
# while i<=end:
#     print('hey!')
#     i+=1

# sum of n numbers
# i=int(input('enter the starting value:'))
# end=int(input('enter the ending value:'))
# sum=0
# while i<=end:
#     sum=sum+i
#     i+=1
# print('the sum is :',sum)

# print even numbers among the given  numbers

# i=int(input('enter the starting number:'))
# end=int(input('enter the ending number:'))
# while i<=end:
#     if i%2==0:
#         print(i)
    # i+=1


# print odd numbers among the given  numbers

# i=int(input('enter the starting number:'))
# end=int(input('enter the ending number:'))
# while i<=end:
#     if i%2!=0:
#         print(i)
#     i+=1

# sum of even numbers

# i=int(input('enter the starting number:'))
# end=int(input('enter the ending number:'))
# sum=0
# while i<=end:
#     if i%2==0:
#         sum=sum+i
#     i+=1
# print('the sum is',sum)

# sum of odd numbers

# i=int(input('enter the starting number:'))
# end=int(input('enter the ending number:'))
# sum=0
# while i<=end:
#     if i%2!=0:
#         sum=sum+i
#     i+=1
# print('the sum is',sum)


# multiplication table

# i=1
# num=int(input('enter the value : '))
# value=0
# while i<=10:
#     value=num*i
#     print(i,'*',num,'=',value)
#     i+=1

i=int(input('enter the starting: '))
end=int(input('enter the ending: '))
sum=0
even=0
odd=0
while i<=end:
    sum=sum+i
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
    i+=1
print('the sum of natural number',sum)
print('the sum of even numbers',even)
print('the sum of odd numbers',odd)

