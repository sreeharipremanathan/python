f=open('python/multi_table.txt','w')
num=int(input('enter a number: '))
product=0
for i in range(1,num+1):
    f.write("\n")
    for j in range(1,11):
        product=i*j
        # print(product)
        print(j,'*',i,'=',product)
        f.write(str(j)+'*'+str(i)+'='+str(product)+'\n')
        # f.write(end="\t")
    # print('\t')
    # print(end="\t")
    