import re
# a='hello'
# print(re.search('h',a))
# print(re.search('hello',a))
# print(re.search('b',a))
# if re.search('h',a):
#     print('match')
# else:
#     print('no match')

# if re.search('ab',a):
#     print('match')
# else:
#     print('no match')

# print(re.search('h',a))
# print(re.search('h.',a))
# print(re.search('e.',a))
# print(re.search('o.',a))
# print(re.search('h..',a))
# print(re.search('h.*',a))
# print(re.search('o.*',a))
# print(re.search('h....',a))
# print(re.search('h.+',a))
# print(re.search('e.+',a))
# print(re.search('l.+',a))
# print(re.search('o.+',a))
# print(re.search('h.?',a))
# print(re.search('e.?',a))
# print(re.search('o.?',a))

# print(re.search('hello',a))
# print(re.search('[hello]',a))
# print(re.search('[a-z]',a))
# print(re.search('[A-Z]',a))
# a='ASUStuf'
# print(re.search('[A-Z]',a))
# print(re.search('[A-z]',a))
# a='aSUStuf'
# print(re.search('[A-z]',a))
# print(re.search('[S-U]',a))

# a='12347'
# print(re.search('[0-9]',a))
# print(re.search('[6-9]',a))

# a='abcd123'
# print(re.search('[a-z][0-9]',a))
# a='1234'
# print(re.search('[a-z][0-9]',a))
# a='abcd'
# print(re.search('[a-z][0-9]',a))
# a='abcd1236'
# print(re.search('[a-z0-9]',a))
# print(re.search('[a-z].*[0-9]',a))
# a='abcd1'
# print(re.search('[a-z].*[0-9]',a))
# print(re.search('[a-z].+[0-9]',a))
# print(re.search('[a-z].?[0-9]',a))
# a='abcd1233'
# print(re.search('[a-z].?[0-9].*',a))
# print(re.search('[a-z].?[0-9].+',a))
# print(re.search('[a-z].?[0-9].?',a))


# mobile number validation

# a='7510552623'
# if len(a)==10 and re.search('[6-9].{9}',a) and a.isdigit():
#     print('valid')
# else:
#     print('not valid')

# email validation

# a='hari@gmail.com'
# print(re.search('^[a-z].*@gmail.com$',a))

# password verification

a=input('enter the password: ')
if len(a)>=8 and re.search('^[A-z0-9].*[@#$&0-9]',a) and not(a.isdigit()):
    print('valid')
else:
    print('not valid')