#Password Generator Project
import random

def uppers_option():
    upper_pas = input("Do you want have uppercase in password. (Yes/No)").lower()
    if upper_pas == "yes":
        upper_amount = int(input("How many uppercase: "))
        return True, upper_amount
    else:
        return False
def lowers_option():
    lower_pas = input("Do you want have lowercase in password. (Yes/No)").lower()
    if lower_pas == "yes":
        lower_amount = int(input("How many lowercase: "))
        return True, lower_amount
    else:
        return False
def numbers_option():
    number_pas = input("Do you want have numbers in password. (Yes/No)").lower()
    if number_pas == "yes":
        number_amount = int(input("How many numbers: "))
        return True, number_amount
    else:
        return False
def symbols_options():
    symbols_pas = input("Do you want have symbols in password. (Yes/No)").lower()
    if symbols_pas == "yes":
        symbols_amount = int(input("How many symbols: "))
        return True, symbols_amount
    else:
        return False



def pass_gen():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    pass_list = []
    password=""
    print("Welcome in the password generator!")

    upper=uppers_option()
    lower=lowers_option()
    number=numbers_option()
    symbol=symbols_options()

    if upper:
        for x in range(upper[1]):
            pass_list.append(random.choice(uppercase))
    if lower:
        for x in range(lower[1]):
            pass_list.append(random.choice(lowercase))
    if number:
        for x in range(number[1]):
            pass_list.append(random.choice(numbers))
    if symbol:
        for x in range(symbol[1]):
            pass_list.append(random.choice(symbols))
    # print(pass_list)
    print(f"Your final password will have {len(pass_list)} characters")
    for character in range(len(pass_list)):
        rand_char=random.choice(pass_list)
        password+=rand_char
        #print(f"Deleting: {rand_char}")
        pass_list.remove(rand_char)

    print(f"Your generated password is: {password}")





