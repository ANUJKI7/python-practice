def count_digits(n):
    count = 0
    while n>0:
        count+=1
        n=n//10
    return count
num=int(input("Enter num:"))
print("number of count:",count_digits(num))