'''Program to input no.s in list and ask user to remove or add element from list'''

a=[]
for i in  range(1,11,1):
        d=int(input("Enter Number:"))
        a.append(d)
print("Number in list:",a)
check=True
while check:
    print("1.Add an element:")
    print("2.Remove an element:")
    print("3.Print")
    print("4.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        y=int(input("Enter element to add:"))
        a.append(y)
    elif(ch==2):
        n=int(input("Enter element to remove:"))
        a.remove(n)
    elif(ch==3):
        print("Altered List:",a)
    elif(ch==4):
        check=False
