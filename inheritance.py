#Inheritance= Kalıtım(Miras alma)
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print('Person created')
    def who_i_am(self):
        print('I am a person')
    def eat(self):
        print("I am eating.")

class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.studentNumber=number
        print("student created")
    #override
    def who_i_am(self):
        print('I am a student')

class Teacher(Person):
    def __init__(self,fname,lname,branch): 
        super().__init__(fname,lname) #super methodu ile self kullanmaya gerek yoktur.
        self.branch=branch
    def who_i_am(self):
        print(f'I am a {self.branch} teacher')
p1=Person('Zeliha','Kıyak')
s1=Student('Burak','Kıyak',7)
t1=Teacher('Semra','karakaya','python')
print(p1.fname+' '+ p1.lname)
print(s1.fname+' '+ s1.lname+' '+str(s1.studentNumber))

p1.who_i_am()
s1.who_i_am()
p1.eat()
s1.eat()
t1.who_i_am()
