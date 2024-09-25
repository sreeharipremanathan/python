# f=open('python/demo_file.txt','r')
# l=f.readlines()
# f.seek(0)
# letters=0
# for i in l:
#     a=f.readline().strip()
#     for i in a:
#         # print(i)
#         if i!=' ':
#             letters+=1
# print(letters)

f=open('python/demo_file.txt','r')
l=f.readlines()
f.seek(0)
cap=0
letters=0
words=0
for i in range(len(l)):
    a=f.readline().strip()
    s=a.split()
    for i in s:
        if i!='':
            words+=1
    for i in a:
        if i!=' ':
            if i.isupper():
                cap+=1
            letters+=1
print(letters)
print('capital',cap)
print('small',letters-cap)
print('words',words)