def total_sum(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    return total
num=int(input("enter num:"))
print("sum of digit:",total_sum(num))