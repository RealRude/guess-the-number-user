# Guess the number (user) 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

print("")
import random

user_number = int(input("Please pick a number between 1 and 10: "))

#import sys
#sys.exit("Stopped.")

print("The user number is: ", user_number)

lower_range = 1
upper_range = 11
computer_guess = random.randrange(lower_range, upper_range)
print("First computer guess is: " + str(computer_guess))
if computer_guess == user_number:
    print("Computer managed the right guess on his first try!")
else:
    while user_number != computer_guess:
        if computer_guess > user_number:

            print("Computer guess: " + str(computer_guess))

            #lowers the upper_range appropriately for another guess cycle
            upper_range = upper_range - (upper_range - computer_guess)

            print(f"The computer guess ({computer_guess}) was too high. Upper range is now: {upper_range}. Now guessing in range from {lower_range} to {upper_range}")

            #let's the computer guess again
            computer_guess = random.randrange(lower_range, upper_range)

        elif computer_guess < user_number:

            print("Computer guess: " + str(computer_guess))

            #raises the lower_range appropriately for another guess cycle
            lower_range = computer_guess + 1

            print(f"The computer guess ({computer_guess}) was too low. Lower range is now: {lower_range}. Guessing in range from {lower_range} to {upper_range}")

            #let's the computer guess again
            computer_guess = random.randrange(lower_range, upper_range)

print("Computer guess: " + str(computer_guess))
print("Computer finally guessed the right number which was: " + str(computer_guess))

endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)


