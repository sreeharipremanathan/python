f=open('multiplication_table_op.txt','w')
num=int(input('enter a number: '))
product=0
for i in range(1,10+1):
    product=num*i
    print(i,'*',num,'=',product)
    f.write(str(i)+'*'+str(num)+'='+str(product)+'\n')