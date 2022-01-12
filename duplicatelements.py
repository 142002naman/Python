a=[]
b=[]
e=[]
for i in range(0,10,1):
    d=int(input("Enter Number:"))
    a.append(d)
for r in a:
    if(r not in b):
        b.append(r)
    else:
        e.append(r)
        print(r)
print("No. of Duplicate Elements:",len(e))
