# def sample(b,*a):
#     print(b,a)
# sample(18)
# sample(1,2)
# sample(1,4,6,7)                            

def sample(**a):
    print(a)

sample(name='hari',age=22,plc='tsr')
sample(name1='hari',age1=22,plc1='tsr',name='achu',age=22,plc='tsr')