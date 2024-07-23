# python object oriented programming
class Employee:
    num_of_emps=0
    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+ '.' +last+ '@company.com'
        Employee.num_of_emps+=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount) 

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

import datetime
my_date=datetime.date(2023,12,13)
print(Employee.is_workday(my_date))

#subclass
class Developer(Employee):
    raise_amt=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay) #iki türlü de olur
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay) #iki türlü de olur
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emps(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emps(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# print(Employee.num_of_emps)    
# emp1=Employee('Corey', 'Schafer', 5000)
# emp2=Employee('Test','User', 6000)
# print(Employee.num_of_emps) 

# emp1.fullname()
# print(Employee.fullname(emp1))
# print(emp2.fullname())
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

dev1=Employee('Corey', 'Schafer', 5000, 'Python')
dev2=Employee('Test','User', 6000, 'Java')

print(dev1.pay)
dev1.apply_raises()
print(dev1.pay)
print(dev1.email)
print(dev2.prog_lang)

mgr1=Employee('Sue','Smith',90000,[dev1])
print(mgr1.email)

mgr1.add_emps(dev2)
mgr1.remove_emps(dev1)
mgr1.print_emps()

print(isinstance(mgr1,Manager))
print(issubclass(Manager,Employee))