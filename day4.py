def print_digits(n):
    while n>0:
        digit= n % 10
        print(digit)
        n=n//10
num= int(input("Enter number:"))
print_digits(num)  