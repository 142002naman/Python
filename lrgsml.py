a=[]
for i in range(0,10,1):
    d=int(input("Enter number:"))
    a.append(d)
g=a[0]
h=a[0]
for r in a:
    if(r>g):
        g=r
    elif(r<h):
        h=r
print("Largest Number from the list is",g)
print("Smallest number from the list is",h)
