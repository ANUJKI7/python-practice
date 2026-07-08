def add(*numbers):
    total=0
    for i in numbers:
        total+=i
    print(total)
add(1,2,3,4)





#from functools import reduce
#nums=[1,2,3,4,5]
#print(reduce(lambda a,b:a*b,nums))