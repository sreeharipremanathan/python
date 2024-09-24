for i in range(3):
    print(i)
    for j in range(4):
        print('\t',j)

# in matrix form
# --------------

# for i in range(3):
#     for j in range(3):
#         print(j,end="\t")
#     print()
    


# to print a 3x3 matrix with values 10,11,12
# ------------------------------------------

# for i in range(3):
#     a=10
#     for j in range(3):
#         print(a,end="\t")
#         a+=1
#     print()


# to print a 7x5 matrix with values 51,52,53,54,55
# ------------------------------------------------

# for i in range(7):
#     a=51
#     for j in range(5):
#         print(a,end="\t")
#         a+=1
#     print()
# output
# 51      52      53      54      55
# 51      52      53      54      55
# 51      52      53      54      55
# 51      52      53      54      55
# 51      52      53      54      55
# 51      52      53      54      55
# 51      52      53      54      55

# for i in range(3):
#     for j in range(3):
#         print(i,end="\t")
#     print()

# out put
# --------
# 0   0   0
# 1   1   1
# 2   2   2


# for i in range(3):
#     for j in range(3):
#         print(i,end="\t")
#         i+=1
#     print()

# output
# -------
# 0       1       2
# 1       2       3
# 2       3       4

# a=0
# for i in range(3):
#     for j in range(3):
#         print(a,end="\t")
#         a+=1
#     print()

# output
# -------
# 0       1       2
# 3       4       5
# 6       7       8


# for i in range(4):
#     if i%2==0:
#         for j in range(3):
#             print(j,end="\t")
#     else:
#             for j in range(3):
#                 print(2-j,end="\t")
#     print()
'''
0       1       2
2       1       0
0       1       2
2       1       0
'''

# for i in range(3):
#     for j in range(3):
#         if j==0:
#             print('A',end="\t")
#         elif j==1:
#             print('B',end="\t")
#         elif j==2:
#             print('c',end="\t")
#     print()

# output
# -------
# A       B       c
# A       B       c
# A       B       c

# a=1
# for i in range(3):
#     for j in range(3):
#         print(a,end="\t")
#         a+=2
#     print()

# output
# -------
'''
1   3   5
7   9   11
13  15  17
'''

# a=1
# for i in range(4):
#     for j in range(4):
#         print(a,end="\t")
#     a+=1


# for i in range(3):
#     a=65
#     for j in range(3):
#         print(chr(a+j),end="\t") 
#     print()

# output
'''
A   B   C
A   B   C
A   B   C
'''

# a=1
# for i in range(1,4):
#     for j in range(i):
#         print(a,end="  ")
#         a+=1
#     print()

# output
# -------
'''
1  
2  3  
4  5  6 
'''

# for i in range(1,4):
#     for j in range(i):
#         print(i-j,end=" ")
#     print()

# output
# -------
'''
1 
2 1 
3 2 1 
'''


# for i in range(3):
#     for j in range(3):
#         if i==j:
#             print(5,end=" ")
#         else:
#             print('#',end=" ")
#     print()

# output
# -------
'''
5 # # 
# 5 # 
# # 5
'''
# a=65
# for i in range(1,4):
#     for j in range(i):
#         print(chr(a+j),end=" ")
#     print()

# output
# -------
'''
A 
A B 
A B C 
'''


# for i in range(1,4):
#     a=64
#     for j in range(i):
#         print(chr(a+i),end=" ")
#     print()

# output
# -----
'''
A 
B B 
C C C 
'''


# for i in range(4):
#     a=64
#     for j in range(i):
#         i-j
#         print(chr((a+i)-j),end=" ")
#     print()

# output
# ------
'''
A 
B A 
C B A
'''
# a=65
# for i in range(4):
#     if i%2==0:
#         for j in range(3):
#             print(j,end="\t")
#     else:
#             for j in range(3):
#                 print(chr(a+j),end="\t")
#     print()

# output
# -------
'''
0       1       2
A       B       C
0       1       2
A       B       C
'''

# l=[2,4,1,5]
# for i in l:
#      print('*'*i)

# output
# ------
'''
**
****
*
*****
'''