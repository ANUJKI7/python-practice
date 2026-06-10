#abstraction second type
# DUCK typing

class teacher:
    def get_desination(self):
        print("desinaiton=teacher")

class accountant:
    def get_desination(self):
        print("desination=accountant")
    
object=teacher()
object.get_desination()

object=accountant()
object.get_desination()


