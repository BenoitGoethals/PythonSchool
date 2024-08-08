import random
import string

words=["Lover","eurika","brussel"]
guess_word:str=random.choice(words)
print(guess_word)
word=[]
for i in guess_word:
    word.append("-")
for i in range(len(guess_word)):
    print(guess_word)
    letter=input("Enter a letter: ")
    if letter in guess_word:
        indexs=[i for i, s in enumerate(guess_word) if letter in s]
        for j in indexs:
            word[j]=letter
    print(word)
    if guess_word.__eq__ (''.join(word)):
        print("You guessed the word!")

