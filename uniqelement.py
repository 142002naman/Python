a=[]
b=[]
for i in range(0,10,1):
    d=int(input("Enter Number:"))
    a.append(d)
for r in a:
    if(r not in b):
        b.append(r)
print(b)
