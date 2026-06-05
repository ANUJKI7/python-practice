class student():
  def __init__(self,name,age,cgpa):
    self.name=name
    self.age=age
    self.cgpa=cgpa
  
  def get_cgpa(self):
    return self.cgpa

s1=student("anuj",22,9.0)
s2=student("adarsh",20,9.8)

print(f"{s1.name} is  {s1.get_cgpa()} year old")
