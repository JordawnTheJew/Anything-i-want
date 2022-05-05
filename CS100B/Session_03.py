class Person:
    def __init__ (self, name='', ID=-1, birthdate ='1/1/2000'):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    def eat(self):
        print("Mmmm, burkfass")


    def sleep(self):
        print('snore')



class Student(Person):
    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        Person.__init__(self, name='', ID=-1, birthdate ='1/1/2000')
        

    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print (self.name + 'is doing homework for thier ' + course + 'course.')

    def ask_question(self):
        print('Wait, what?')

    def eat(self):
        print('Mmmm, dinner')

    def sleep(self):
        print('snore')

stud = Student ('George', 100, '2/1/1860')
stud.sleep()
stud.study()
stud.eat()

class Teacher(Person):

    def __init__(self, name='', ID=-1, birthdate='1/1/2000'):
        Person.__init__(self, name='', ID=-1, birthdate ='1/1/2000')
         

    def teach(self):
        print(self.name + ' is teaching')

    def assign_homework(self, course):
        print(self.name + ' assigned homewokr for thier ' + course + ' course')

    def answer_question(self):
        print('Ler me see if i can help')

    def eat(self):
        print('Mmm, dinner')

    def sleep(self):
        print("Snore")

    def birthdate(self):
        print(self.birthdate)



teach = Teacher ('Martha', 101, "9/1/1975")
teach.sleep
teach.teach()
Teacher.birthdate
        
        