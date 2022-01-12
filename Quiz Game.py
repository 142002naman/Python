c=0
print("Note:")
print("1.Negitive marking will be done if type wrong input")
print()
print()
print()
print("Which is the most sensitive organ in our body?")
print("1.eyes  2.tongue 3.nose  4.Skin")
ch=int(input("Type the correct option NO:"))
if(ch==4):
    c=c+1
elif(ch>4):
    print()
    print("Negitive marking for wrong input")
    c=c-1
print()
print("Giddha is the folk dance of?")
print("1.Maharashtra  2.Rajasthan  3.Punjab  4.Gujrat")
a=int(input("Type the correct option NO:"))
if(a==3):
    c=c+1
elif(a>4):
    print()
    print("Negitive marking for wrong input")
    c=c-1
print()
print("Who was the first Prime Minister of India?")
print("1.Jawahlal Nehru  2.Narendra Modi  3.Mahatma Gandhi  4.Bhagat Singh")
b=int(input("Type the correct option NO:"))
if(b==1):
    c=c+1
elif(b>4):
    print()
    print("Negitive marking for wrong input")
    c=c-1
print()
print("Who was the first President of India?")
print("1.Dr. B.R. Ambedkar  2.Dr. Rajendra Prasad  3.Bhagat Singh  4.none of these")
d=int(input("Type the correct option NO:"))
if(d==2):
    c=c+1
elif(d>4):
    print()
    print("Negitive marking for wrong input")
    c=c-1
print()
print("Which one of the following river flows between Vindhyan and Satpura ranges?")
print("1.Narmada  2. Mahanadi  3.Netravati  4.Son")
e=int(input("Type the correct option NO:"))
if(e==1):
    c=c+1
elif(e>4):
    print()
    print("Negitive marking for wrong input")
    c=c-1
if(c==5):
    print()
    print()
    print("You won")
else:
    g=5-c
    print()
    print()
    print("You Lose,Your score are",c,"numbers")
