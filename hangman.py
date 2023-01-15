import random

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

word_list = [
'coincide',
'problem',
'background',
'self',
'calculation',
'economic',
'money',
'grimace',
'satellite',
'castle',
'autonomy',
'expenditure',
'acquit',
'marble',
'extend',
'houseplant',
'admission',
'splurge',
'easy',
'prosecute',
]

def hangman_game():
        print(logo)
        print("Welcome in the hangman game!")
        print("Now a random word is generated")
        random_word = list(random.choice(word_list))
        your_word = ''.join(random_word)
        length_word = len(random_word)
        display = []
        off = False
        lifes = 6

        for x in range(length_word):
                display.append("_")

        print(display)

        while not off:

                guess = input("Guess a letter: ").lower()

                if guess not in random_word:
                        if lifes <= 0:
                                print("You lost")
                                off = True
                        else:
                                print(f"You're wrong, you lost one life. Try again guess the letter.\nRemaining {lifes}")
                        print(stages[lifes])
                        lifes -= 1

                for x in range(length_word):
                        if guess == random_word[x]:
                                random_word[x]="_"
                                display[x] = guess
                print(display)
                if ''.join(display) == your_word:
                        print(''.join(display))
                        print(f"You won. You have kept {lifes + 1} lifes")
                        off = True






