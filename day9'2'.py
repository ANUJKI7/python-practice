#write read operation

f=open("sample.txt","w+")
f.write("this is my first programmm")

f.seek(0)
print(f.read())
f.close()