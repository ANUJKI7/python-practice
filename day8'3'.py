#abstraction second type
# DUCK typing

class teacher:
    def get_desination(self):
        print("desinaiton=teacher")

class accountant:
    def get_desination(self):
        print("desination=accountant")
    
teacher=teacher()
teacher.get_desination()

accountant=accountant()
accountant.get_desination()


