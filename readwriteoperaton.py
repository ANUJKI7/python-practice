#read operation
f=open("sample.txt","r")
data=f.read()
print(data)
f.close()

#readline operation(in this it can read only one line)
f=open("sample.txt","r")
data=f.readline()
print(data)
f.close()

#write operation
f=open("sample.txt","w")
f.write("what is the name  of the first person")
f.close()

#append operation
f=open("sample.txt","a")
f.write("\ni am Thomos shelby")
f.close()




