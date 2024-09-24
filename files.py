# f=open('python/demo_file.txt','x')
# f.write('hey there....')
# f=open('python/demo_file.txt','r')
# a=f.read(4)
# f.seek(0)
# b=f.read()
# print(f.tell())
# print(a)
# print('-'*20)
# print(b)
# print(f.read())
# a=f.readline(4)
# b=f.readline()
# f.seek(0)
# c=f.readlines()
# print(a)
# print(b)
# print(c)


# f=open('python/demo_file.txt','r')
# l=f.readlines()
# f.seek(0)
# for i in range(len(l)):
#     a=f.readline().strip()
#     # print(a)
#     rev=''
#     for j in a:
#         rev=j+rev
#     print(rev)


f=open('python/demo_file.txt','w')
f.write('ohayo')
a=open('demo1.txt','w')
a.write('good morning')
a.write('\nohayo')

b=open('deno2.txt','a')
b.write('thanks\n')
b.write('arigato')