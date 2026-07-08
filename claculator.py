def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operator=input("enter the choice of operation +,-,*,/:")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if operator=="+":
 print(add(num1,num2))
 
 
elif operator=="-":
 print(subtract(num1,num2))
 

elif operator=="*":
   print(multiply(num1,num2))
 
elif operator=="/":
   if num2==0:
      print("cannot divided by 0")
   else:
      print(float(divide(num1,num2))) 
else:
   print("invalid operator")