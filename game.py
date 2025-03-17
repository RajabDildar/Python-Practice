# Guess the number game
import random  
random_number = random.randint(1, 100)  
guess_count = 0

while True:
    try:
        user_number = int(input("Guess a number between 1 - 100 : "))
        guess_count += 1
        if(random_number > user_number):
            print(f"Your number is too low, please guess a higher number")
        elif(random_number < user_number):
            print(f"Your number is too high, please guess a lower number")
        else:
            print(f"Congratulations! You successfully guessed the number in {guess_count} guesses")
            break
    except ValueError:
        print("Please enter a valid number")
