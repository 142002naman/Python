'''Program to input no. and return factorial of that no.'''

def fact(no):
    b=1
    for i in range(1,no+1,1):
        b=b*i
    return b
no=int(input("Enter number"))
v=fact(no)
print(v)
