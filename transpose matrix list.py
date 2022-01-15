a=[]
for i in range(0,3,1):
    b=[]
    print("Enter number for",i,"row")
    for j in range(0,3,1):
        c=int(input("Enter number"))
        b.append(c)
    a.append(b)
for i in range(2,0-1,-1):
    for j in  range(2,0-1,-1):
        print(a[i][j],end='')
    print()
