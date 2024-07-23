class Person:
    #class attribute
    address='no information'
    #constructor method
    def __init__(self,name,year):
        #object attributes
        self.name=name #this.name=name
        self.year=year #this.year=year de denilebilir
    #instance methods
    def intro(self):
        print('hello there i am '+ self.name)
    def calculateAge(self):
        return 2023-self.year

     
#object(instance)
p1=Person('Zeliha',2003)
p2=Person('Zeynep',2005)
#updating
p1.name='Seyma'
p1.address='Corum'
#accessing object attributes
print(f'p1 name:{p1.name} year:{p1.year}')
print(f'p2 name:{p2.name} year:{p2.year}')
p1.intro()

print(f'Adım: {p1.name} ve yaşım:{p1.calculateAge()}')
print(f'Adım: {p2.name} ve yaşım:{p2.calculateAge()}')
