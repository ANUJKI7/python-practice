class teacher: #multiple inhertence
    def __init__(self,salary):
        self.salary=salary
class student:
    def __init__(self,gpa):
        self.gpa=gpa
class ta(teacher,student):
    def __init__(self,name,salary,gpa):
        super().__init__(salary)
        student.__init__(self,gpa) # this the way for direct access class
        self.name=name
per1=ta(1000,9.8,"anuj")
print(per1.name,per1.salary,per1.gpa)
    
