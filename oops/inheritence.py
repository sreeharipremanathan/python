#single inheritance
# ====================

# class synnefo:
#     def php(self):
#         print('php std')
#     def python(self):
#         print('python std')

# class novavi(synnefo):
#     def web_dev(self):
#         print('web dev wrks')
#     def digital_marketing(self):
#         print('dm wrks')

#a staff came to novavi
# staff=novavi()
# staff.web_dev()
#then stafff wants to study python
# staff.python()

#staff in novavi can access synnefo
# std=synnefo()
#std can't access novavi



# class parent:
#     def car(self):
#         print('car')
#     def shop(self):
#         print('shop')

# class child(parent):
#     def bike(self):
#         print('bike')

# father=parent()
# father.car()
# father.shop()

# son=child()
# son.shop()
# son.car()
# son.bike()

# multiple inheritance
#--------------------
# class father:
#     def shop(self):
#         print('shop')
#     def car(self):
#         print('car')

# class mother:
#     def money(self):
#         print('money')
#     def mobile(self):
#         print('mobile')

# class child(father,mother):
#     def bike(self):
#         print('bike')

# son=child()
# son.bike
# son.mobile
# son.car


# class kia:
#     def sonet(self):
#         print('sonet')
#     def seltos(self):
#         print('seltos')

# class ducati:
#     def scrambler(self):
#         print('scrambler')
#     def panigale(self):
#         print('panigale')

# class customer(kia,ducati):
#     def money(self):
#         print('money')

# abi=customer()
# abi.scrambler()
# abi.seltos()


# class school:
#     def class_from_school(self):
#         print('class')
#     def school_ground(self):
#         print('ground')

# class tuition:
#     def notes(self):
#         print('notes')
#     def work_space(self):
#         print('work space')

# class student(school,tuition):
#     def uniform(self):
#         print('uniform')

# athi=student()
# athi.class_from_school
# athi.notes

# class university:
#     def exams(self):
#         print('exams')
#     def results(self):
#         print('results')


# class clg(university):
#     def classes(self):
#         print('classes')
#     def notes(self):
#         print('notes')

# class std(clg):
#     def id_card(self):
#         print('id card')

# hari=std()
# hari.exams()
# hari.classes()
# hari.id_card()

#hirearchial 
class  school:
    def exams(self):
        print('exams')
    def results(self):
        print('results')

class class1(school):
    def notes(self):
        print('notes class1')
    def class_room(self):
        print('class dtls')

class class2(school):
    def notes(self):
        print('notes class2')
    def class_room(self):
        print('class dtls')

std1=class1()
std1.exams()
std1.notes()

std2=class2()
std2.notes()
std2.results