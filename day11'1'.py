num1=float(input("Enter the num:"))
operator=input("Enter the operator(+,-,*,/):")
num2=float(input("Enter the num:"))
 
if operator == "+":
    print("Result:",num1+num2)

elif operator == "-":
    print("Result:",num1-num2)

elif operator == "*":
    print("Result:",num1*num2)

elif operator == "/":
    if num2 == 0:
        print(" number not divided by 0")
    else:
     print("Result:",num1/num2)
else:
    print("invlaid opeartor")

