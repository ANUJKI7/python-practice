def average(*numbers):
   total=0
   for i in numbers:
      total=total+i
   return total/len(numbers)
c=average(2,3,4,5)
print(c)