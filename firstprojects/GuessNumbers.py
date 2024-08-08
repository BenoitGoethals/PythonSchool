import random

HARD=10
EASY=5

print("Welcome to guess the number!")

print("I thinking of number between 1 -100")
difficulty=input("Chouse a difficulty (e)asy or (h)ard").lower()
guess_max=0
NotGuested=True;
if(difficulty=="e"):
    guess_max=EASY
count=0
computer_number=random.randint(1,100)
while count<guess_max and NotGuested:
    guess=int(input("Guess a number: "))
    count+=1
    if(guess<computer_number):
        print("Sorry you guessed too low")
    elif(guess>computer_number):
        print("Sorry you guessed too high")
    elif(guess==computer_number):
        print("You got it!")
        NotGuested=False
    print(f"You have {guess_max-count} attemps")
if(count==guess_max):
    print("You lose")
else:
    print("Congrats!")