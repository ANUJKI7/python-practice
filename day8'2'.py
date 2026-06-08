# polymporphsim example

class employee:  #function overriding
    def get_desination(self):
        print("desination=employee")

class teacher(employee):
    def get_desination(self):
        print("desianiton=teacher")

teacher=teacher()
teacher.get_desination()