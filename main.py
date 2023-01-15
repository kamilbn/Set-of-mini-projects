import calculator as calc
import password_generator as pswd
import simpler_password_generator as simpler_pswd
import hangman
print("Welcome in the set of applications.\nThis program contains some mini programs ready to use.")
print("Available programs:\n1. Password generator.\n2. Simpler Password generator.\n3. Caesar cipher.\n4. Hangman.\n5. "
      "Calculator. ")
option=input("Enter the number of program which you want launch: ")

match option:
    case "1":
        pswd.pass_gen()
    case "2":
        simpler_pswd.simpler_pass_gen()
    case "3":
        pass
    case "4":
        hangman.hangman_game()

