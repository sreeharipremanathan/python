lms=[]
# id=100
def register():
    # id=+1
    id=int(input('enter ypur id: '))
    name=input('enter your name: ')
    place=input('enter your place: ')
    address=input('enter your address: ')
    mob=int(input('eneter your mobile number: '))
    password=input('set your password: ')
    lms.append({'id':id,'name':name,'place':place,'address':address,'mobile_no':mob})
    print('registration successfull')
def login():
    uname=input('enter your name: ')
    password=input('enter your passsword')
    f=0
while True:
    print('''
            1.register
            2.login
            3.exit
''')
    choice=int(input('enter your choice'))
    if choice==1:
        register()