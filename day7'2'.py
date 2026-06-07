class employes: #inhertance
    start_time="9am"
    end_time="5pm"
class teacher(employes):
    def __init__(self,subject):
        self.subject=subject
teacher1=teacher("maths")
print(teacher1.subject,teacher.start_time,teacher1.end_time)

