import random

def simpler_pass_gen():
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    password=""

    while True:

        print("""
        ██████   █████  ███████ ███████ ██     ██  ██████  ██████  ██████       ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  
        ██   ██ ██   ██ ██      ██      ██     ██ ██    ██ ██   ██ ██   ██     ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
        ██████  ███████ ███████ ███████ ██  █  ██ ██    ██ ██████  ██   ██     ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  
        ██      ██   ██      ██      ██ ██ ███ ██ ██    ██ ██   ██ ██   ██     ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ 
        ██      ██   ██ ███████ ███████  ███ ███   ██████  ██   ██ ██████       ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ 
            """)
        print("Welcome in the simpler password generator!")
        length=int(input("Enter the length of password: "))

        for x in range(length):
            password+=random.choice(characters)
        print(f"Your final password will have {length} characters")
        print(f"Your generated password is: {password}")
        action = input(" If you want generate password again type: 'yes' or anything else to exit: ").lower()
        if action == 'yes':
            simpler_pass_gen()
        else:
            break
