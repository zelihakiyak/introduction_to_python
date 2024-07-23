class Person:
    predefined_courses=['Com101','Com201','Com301']
    def __init__(self,first_name,last_name,age,department):
        self.fname=first_name
        self.lname=last_name
        self.age=age
        self.department=department

class Student(Person):
    def __init__(self,first_name,last_name,age,department,studentNo):
        super().__init__(first_name,last_name,age,department)
        self.studentNo=studentNo
    def get_student_id(self):
        return self.studentNo
    def control_and_add_course(self):
        pass 
    

class Graduate(Person): 
    def __init__(self,first_name,last_name,age,department):
        super().__init__()
    def get_graduation_year(): #Mezuniyet yılını döndürmek için kullanılır. 
        pass

    def get_graduation_gpa():  #Mezuniyet not ortalamasını döndürmek için kullanılır. 
        pass



class Instructor(Person):
    def __init__(self,first_name,last_name,age,department):
        super().__init__()

    def get_main_branch(): #Eğitmenin uzmanlık alanını döndürmek için kullanılır.
        pass