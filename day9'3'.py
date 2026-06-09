#append read operation

f=open("sample.txt","a+")
f.write("\n i am anuj kumar")
f.seek(0)
print(f.read())
f.close()