class employes: #multi level inheritence example
    start_time="9am"
    end_time="5pm"
class teacher(employes):
    def __init__(self,subject):
        self.subject=subject
class accountant(teacher):
    def __init__(self,role,subject):
        super().__init__(subject)
        self.role=role
acc1=accountant("ca","teacher")
print(acc1.role,acc1.subject,acc1.start_time,acc1.end_time)

