# num=int(input("enter a number: "))
# numbers={0:'zero ',1:'one ',2:'two ',3:'three ',4:'four ',5:'five ',6:'six ',7:'seven ',8:'eight ',9:'nine '}
# s=''
# while num>0:
#     t=num%10
#     s=numbers[t]+' '+s
#     num//=10
# print(s)

l=[{'name':'hari','age':20,'lang':['eng','mal']}]
lng=input('enter the language')
l[0]['lang'].append(lng)
print(l)