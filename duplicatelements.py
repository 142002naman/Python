'''Program to input no.s in list and find duplicate elements from the list'''

a=[]
b=[]
e=[]
for i in range(0,10,1):
    d=int(input("Enter Number:"))
    a.append(d)
print("Duplicate elements from list are as following:")
for r in a:
    if(r not in b):
        b.append(r)
    else:
        e.append(r)
        print(r)
print("No. of Duplicate Elements:",len(e))
