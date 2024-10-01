d={1:'sun',2:'mon',3:'tue'}

def swap(d):
    # d1={}
    # for i in d:
    #     d1[d[i]]=i
    # return d1
    return{value:key for key,value in d.items()}
print(swap(d))