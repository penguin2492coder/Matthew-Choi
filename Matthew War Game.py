'''anything=["Lacrosse",29,True,4.32]
print(anything[1])
anything.append("stuff")
print(anything)
anything.remove("Lacrosse")
print(anything)'''

import random

print("Welcome to the number war game!")
myHand=[]
compHand=[]

for i in range(10):
    myHand.append(random.randint(1,100))
    compHand.append(random.randint(1,100))

print("Here is your hand:")
print(myHand)
print("Here is my hand:")
print(compHand)

myScore=0
compScore=0

for i in range(10):
    print("Here is your updated hand:")
    print(myHand)
    choice=int(input("What number do you want to play? "))
    while choice not in myHand:
        choice=int(input("What number do you want to play? "))
    print("you played a",choice)
    myHand.remove(choice)
    compChoice=random.choice(compHand)
    compHand.remove(compChoice)
    print("I chose",compChoice)
    if choice>compChoice:
        print("You won this round")
        myScore+=2
    elif choice<compChoice:
        print("You lost this round")
        compScore+=2
    else:
        print("Tie")
        compHand.append(compChoice)
        myHand.append(choice)
if myScore>compScore:
    print("you won this war")
else:
    print("I won this war")

