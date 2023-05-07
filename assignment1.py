#importing the random module
import random

#defining a function to generate a random number between 1 and 6 which are the sides of the dice
def random_number():
    number = random.randint(1,6)
    print("The number is: ", number)

#calling the function first to generate the first roll number
random_number()

#a while loop to keep rolling until the user doesn't want to roll again. At every roll, a number is generated and printed.
while True:
    roll_again = input("Would you like to roll again? (yes or no): ")
    if roll_again == "yes":
        random_number()
    elif roll_again == "no":
        break
    else:
        print("Please enter yes or no")

        
