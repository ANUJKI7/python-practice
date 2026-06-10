class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)
        print()

p1 = Person("Anuj")
p2 = Person("Anuj", 22)
p3 = Person("Anuj", 22, "Greater Noida")

p1.display()
p2.display()
p3.display()