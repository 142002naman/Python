'''Program to play stone paper scissor game with computer'''

import random
print("Program to play stone paper scissor")
print()
print()
print()




def run():
    comp = 0
    user = 0
    back = True
    while back:
        print("1.Stone")
        print("2.Scissor")
        print("3.Paper")
        print("4.Exit")
        a=int(input("Enter your choice:"))
        r=random.randint(1,4)
        
        if(a==1):
            if(r==3):
                comp=comp+1
            elif(r==2):
                user=user+1
        elif(a==2):
            if(r==1):
                comp=comp+1
            elif(r==3):
                user=user+1
        elif(a==3):
            if(r==1):
                user=user+1
            elif(r==2):
                comp=comp+1
        
        if a==4:
            back =  False
        
        print("\n")
        if a>4:
            print("please choose number between 1 to 3")
        else:
            print(f"computer won the game {comp} time")
            print(f"user won the game {user} time")
        print("\n")


run()
print("press 5 for start the game again")

num = int(input())

if(num == 5):
    run()
else:
    exit()
