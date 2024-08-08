#questions
import random
import os
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


questions = {"What is the city born parents?": "Gent",
             "What is the most common surname in the United States": "smith",
             "How many faces does a Dodecahedron have": "12",
             "Who was the last Tsar of Russia": "Nicholas ",
             "Who discovered that the earth revolves around the sun": "Copernicus",
             "Which planet has the most moons": "Saturn",
             "How many dots appear on a pair of dice": "42",
             "What planet is closest to the sun": "Mercury",
             "What is the city born children?": "Gent",
             "What is the city born friends?": "Gent",
             "2 *4": "8"}
max = len(stages)
bad_answer = 0
good_answer = 0
counter = 0

print(logo)
while bad_answer < max and counter < max:
    picked_question = random.choice(list(questions.keys()))
    print(picked_question)
    answer = input("Answer? : ")
    counter += 1
    if not questions.get(picked_question) == answer:
        bad_answer += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(stages[len(stages)-bad_answer])
        print("Bad Answer")
    else:
        good_answer += 1
        print("Good Answer")

if(bad_answer < max):
    print("Congratulations!")
else:
    print("Sorry your dead")
print(f"bad answer {bad_answer}")
print(f"good answer {good_answer}")
