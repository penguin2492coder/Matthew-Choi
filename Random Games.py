import random

'''print("welcome to the fortune teller")
print("your fortune is...")
random=random.randint(1,5)

if random==1:
      print("you will win the lottery!")
elif random==2:
    print("you will live to 100!")
elif random==3:
    print("you will be cursed for life!!")
elif random==4:
    print("you will get your dream job.")
elif random==5:
    print("world war 3 is your fault!")'''

print("let's play some guessing games")
    

password="Lacrosse"

guess=input("Guess the password:")

while guess!=password:
    guess=input("This is easy, try again.")
if guess==password:
    print("nice job!")
print("now you can play the guessing game.")
print("this number guessing game will need you to find my hidden number.")
number=random.randint(1,100)
score=1
guess=int(input("Guess the number from 1-100: "))

while guess!=number:
    score=score+1
    print("incorrect.")
    if guess>number:
        print("to high.")
    elif guess<number:
        print("to low.")
    guess=int(input("Guess again."))

print("good job you got it, the number was",number)
print("it took you",score,"tries. Nice!")
