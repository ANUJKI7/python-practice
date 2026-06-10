from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def calculate_salary(self):
        print("Intern Salary = ₹10,000")


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("Full Time Employee Salary = ₹50,000")


class ContractEmployee(Employee):
    def calculate_salary(self):
        print("Contract Employee Salary = ₹30,000")


i = Intern()
f = FullTimeEmployee()
c = ContractEmployee()

i.calculate_salary()
f.calculate_salary()
c.calculate_salary()