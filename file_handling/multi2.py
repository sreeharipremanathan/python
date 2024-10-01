f=open('python/multi_table.txt','w')
num=int(input('enter a number: '))
product=0
for i in range(1,11):
    for j in range(1,num+1):
        product=i*j
        print(j,'*',i,'=',product)
        f.write(str(j)+'*'+str(i)+'='+str(product)+'\t')
    f.write("\n")   