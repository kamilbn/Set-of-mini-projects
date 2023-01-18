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

██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██ 
██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██ 
███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██ 
██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██ 
██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████ 
                                                                                                                           
    '''

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

    lifes = 6

    for x in range(length_word):
        display.append("_")

    print(display)

    while True:

        guess = input("Guess a letter: ").lower()

        if guess not in random_word:
            if lifes <= 0:
                print(stages[lifes])
                print("You lost.")
                action1 = input(" If you want play again type: 'yes' or anything else to exit: ").lower()
                if action1 == 'yes':
                    hangman_game()
                else:
                    break


            else:
                print(f"You're wrong, you lost one life. Try again guess the letter.\nRemaining {lifes}")
            print(stages[lifes])
            lifes -= 1

        for x in range(length_word):
            if guess == random_word[x]:
                random_word[x] = "_"
                display[x] = guess

        if guess in your_word:
            print(f"You already guessed the letter: {guess}, type another")

        print(display)
        if ''.join(display) == your_word:
            print(''.join(display))
            print(f"You won. You have kept {lifes + 1} lifes")
            action = input(" If you want play again type: 'yes' or anything else to exit: ").lower()
            if action == 'yes':
                hangman_game()
            else:
                break
