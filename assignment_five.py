#Sofia Fall
# 12/15/22
# Guessing Game
import random


def generate_random_number():
    """
    This function generates and returns a random number ranging from 1 to 100
    """
    return random.randint(1, 100)


def play_guessing_game():
    """This function generates a random number and initializes a counter variable,
    then prompts the user to enter a guess and determines if the guess is correct or incorrect.
    If the guess is correct, the function prints a success message, otherwise
    the function prompts the user for additional input and repeats this process until the guess is correct."""
    number = generate_random_number()  # Generate random number
    counter = 0  # Initialize a counter variable

    # Prompt user to enter a number
    print("This is a guessing game. Please enter a number to begin: ")

    guess = int(input())  # Collect user input
    counter += 1  # Increment the counter

    # Determine if the guess is correct or incorrect
    while True:

        # If the guess is correct
        if guess == number:
            print("You guessed correctly! It took you", counter, "tries.\n\n")
            break

        # If the guess is incorrect
        if guess > number:
            # Prompt user to enter a number
            print("That's far too high, please guess lower: ")
            guess = int(input())  # Collect user input
            counter += 1  # Increment the counter
        if guess < number:
            # Prompt user to enter a number
            print("That's far too low, please guess higher: ")
            guess = int(input())  # Collect user input
            counter += 1  # Increment the counter


def main():
    for x in range(3):
        print("GAME ", (x + 1))
        print()
        play_guessing_game()
    print("Thanks for playing!")


main()