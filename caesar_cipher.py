letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z' ]

logo = """
   _____                                  _       _               
  / ____|                                (_)     | |              
 | |     __ _  ___  ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                           | |                    
                                           |_|                    
"""


def encryption(shift):
    message=input("Provide your message: ").lower()
    encrypt_message=""

    for x in range(len(message)):
        if message[x] in letters:
            index=letters.index(message[x])
            next = index + shift
            if next >= len(letters):
                next = next - len(letters)
            encrypt_message+=letters[next]
        elif message[x] == ' ':
            encrypt_message+=' '
    print(f"Your encoded message is: {encrypt_message}")


def decryption(shift):
    message = input("Provide your message: ").lower()
    decrypt_message = ""

    for x in range(len(message)):
        if message[x] in letters:
            index = letters.index(message[x])
            next=index-shift

            decrypt_message += letters[next]

        elif message[x] == ' ':
            decrypt_message += ' '
    print(f"Your encoded message is: {decrypt_message}")

def again():


    again = input("Type 'yes' if you want again. Otherwise type whatever to exit: ").lower()
    if again == "yes":
        cipher()
    else:

        print("Thank for using the program. Goodbye")


def cipher():



        print(logo)
        print("Type 'encode' to encrypt, type 'decode' to decrypt:")
        option=input().lower()


        if option == 'encode' or option == 'decode':
            shift = int(input("Type the number of shift: "))
            shift = shift % 26
            if option == 'encode':
                encryption(shift)
                again()
            elif option == 'decode':
                decryption(shift)
                again()
        else:
            print("You provided wrong value, please try again!")
            cipher()




