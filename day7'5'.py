class student:
    def __init__(self,name,rollno,marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    def get_name(self):
            return self.__name
    def get_rollno(self):
          return self.__rollno
    def get_marks(self):
          return self.__marks
    def set_name(self,new_name):
     if new_name.strip() !="":
          self.__name=new_name
     else:
        print("name can not be empty")
    def set_rollno(self,new_rollno):
        if 1 <=new_rollno <=100:
            self.__rollno=new_rollno
        else:
         print("roll no can to negative and more than 100")
    def set_marks(self,new_marks):
        if new_marks>=0:
            self.__marks=new_marks
        else:
            print("marks can not be negative")
            
sutd1=student("anuj",20,300)
sutd1.set_rollno(25)
sutd1.set_marks(360)

print(sutd1.get_rollno(),sutd1.get_name(),sutd1.get_marks())
