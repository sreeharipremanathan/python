# class copmany():
#     def accounts(self):
#         print('account dtls')

# class staff(copmany):
#     def accounts(self):
#         print('staff accounts')

# achu=staff()
# achu.accounts()

# class school():
#     def notes(self):
#         print('notes')
# class students(school):
#     def notes(self):
#         print('std notes')

# std1=students()
# std1.notes()

class library():
    def __init__(self):
        print('book dtls')

class user(library):
    def __init__(self):
        print('user dtls')

user1=user()