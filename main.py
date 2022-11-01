# Guess the number (user) 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

print("")
import random

user_number = int(input("Please pick a number between 1 and 10: "))

#import sys
#sys.exit("Stopped.")

print("The user number is: ", user_number)

computer_guess = random.randrange(1, 11)
print("First computer guess is: " + str(computer_guess))
if computer_guess == user_number:
    print("Computer managed the right guess on his first try!")
else:
    while user_number != computer_guess:
        if computer_guess > user_number:

            print("Computer guess:" + str(computer_guess))
            show_range = computer_guess - 1
            print(f"The computer guess ({computer_guess}) was too high. Now guessing in range from 1 to " + str(show_range))
            computer_guess = random.randrange(1, computer_guess)

        elif computer_guess < user_number:

            print("Computer guess:" + str(computer_guess))
            show_range = computer_guess + 1
            print(f"The computer guess ({computer_guess}) was too low. Guessing in range from " + str(show_range) + " to 11")
            computer_guess = random.randrange(computer_guess, 11)

print("Computer guess:" + str(computer_guess))
print("Computer finally guessed the right number which was: " + str(computer_guess))

endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)


