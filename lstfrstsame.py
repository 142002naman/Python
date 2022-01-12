a=[]
for i in range(0,10,1):
    d=input("Enter Name:")
    a.append(d)
for r in a:
    b=len(r)
    if(r[0]==r[b-1]):
        print(r)
