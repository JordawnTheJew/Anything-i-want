"""
class Student:
    name='Any'
    ID = -1
    birthdate = '1/1/2000'

stud=Student()
stud.name='Mary'
stud.ID=10101
stud.birthdate='1/1/1999'

stud2=Student()
stud2.name = 'Gabs'

stud3=Student()
stud3.name='CaiahHammer'

print(stud.ID,"\n",stud.birthdate,"\n",stud2.name, '\n', stud3.name)


class Teacher:
    name= ''
    subject= ''
    courseDate= ''
    roomnumber= -1

Pete=Teacher()
Pete.name='Peter Quill'
Pete.subject ="CS100"
Pete.courseDate= "2/16/2022"
Pete.roomnumber = 216

print(Pete.name, Pete.subject, Pete.courseDate, Pete.roomnumber)

class course:
    name=''
    roster=[]
    teach=teacher=()

s = Student()
s2 = Student()
s2.name = 'Mark'
s3 = Student()
s3.name ='Jill'
s4 = Student()
s4.name = "Martha"
s5 = Student()
s5.name = 'Steve'

c = course()

c.roster = [s, s2, s3, s4, s5]

for stud in c.roster:
    #
    # 
    
    print("Welcome")
    #print("\t#" + str(stud.ID) + " -- " + stud.name)
    if stud.name.startswith('M'):
        print (stud.name + "'s starts with M")
"""

class Student:
    name = ''
    ID = -1
    birthdate = '1/1/20202'

    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print(self.name + ' is doing homework for thier ' + course + ' course')
    
    def ask_question(self):
        print("Wait, what?")


stud = Student()
stud.name = 'Mary'
stud.ID = 10101
stud.birthdate = '1/1/1999'

print(stud.name)

stud.study()
stud.do_homework('CS100A')
stud.ask_question()