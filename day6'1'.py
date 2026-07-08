class Student:
    def __init__(self,name,rollno,gender,cgpa):
        self.name=name
        self.rollno=rollno
        self.gender=gender
        self.cgpa=cgpa
        
s1=Student("anuj",23,"male",7.4)
s2=Student("adarsh",24,"male",8.5)
s3=Student("ayush",25,"male",8.6)

print(f"{s2.name} is {s1.gender} and he got {s3.cgpa} in clg")