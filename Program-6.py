'''Program to check if inputted no. is fibonacci or not'''

n1=0
n2=1
f=0
n = int(input("Enter number:"))
for i in range(0,n+3,1):
       nth = n1 + n2
       n1 = n2
       n2 = nth
       if(n1==n or n1==0):
           f=1
           print("fibonacci")
           break
if(f==0):
    print("Not Fibonacci")
