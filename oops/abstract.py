from abc import ABC,abstractmethod
class syneefo(ABC):
    @abstractmethod
    def reg(self):
        pass
    def python(self):
        print('python dlts')
    def php(self):
        print('php dtls')

class staff(syneefo):
    def reg(self):
        print('staff dtls')
    def notes(self):
        print('notes')

class std(syneefo):
    def reg(self):
        print('std dtls')
    def exams(self):
        print('exams')
        
# staff1=staff()
# staff1.reg()

std1=std()
std1.reg()
std1.exams()