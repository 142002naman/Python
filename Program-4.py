'''Program to input no.s in list and print even and odd from list'''

d=[]
g=[]
e=[]
for i in range(0,10,1):
    a=int(input("Enter number"))
    d.append(a)
for r in d:
    if(r%2==0):
        g.append(r)
    else:
        e.append(r)
print(g)
print(e)
