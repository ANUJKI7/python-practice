class employes: #inhertance
    start_time="9am"
    end_time="5pm"
    def change_time(self,newend_time):
        self.end_time=newend_time
class teacher(employes):
    def __init__(self,subject):
        self.subject=subject
class staff(employes):
    def __init__(self,role):
        self.role=role
staff1=staff("manager")
teacher1=teacher("maths")
teacher1.change_time(6)
print(teacher1.subject,staff1.role,teacher.start_time,teacher1.end_time)

