# Sofia
# 12/15/22
# Guessing Game
import random
import array
from time import sleep
import sys
import os
import time


def clear():                   # Defines the clear () function
    """ Clear terminal. """

    os.system('clear')         # Clears the terminal screen


print ("\n")
for i in range(31):
    sys.stdout.write('\r')                                          # Write a carriage return (\r) to move the cursor to the beginning of the line
    sys.stdout.write("[%-30s] %+3s%%" % ('='*i, round(3.333*i)))    # The number of equals signs that are filled in represents the progress as a percentage, The progress percentage is calculated by multiplying i by 3.333 and rounding it to the nearest integer
    sys.stdout.flush()                                              # Flush the output buffer
    sleep(0.13)                                                     # Pause for 0.13 seconds
    clear()                                                         # Clear the terminal



def delprint(text: str = "Type a string in", delay_time: int = .05):                # Defines delayed print function
    """This function prints the given text with a delay between each character."""
    for character in text:                                                          # For each character in the string
        sys.stdout.write(character)                                                 # Writes the character
        sys.stdout.flush()                                                          # Flushes the output buffer
        time.sleep(delay_time)                                                      # This is the delay time between each character


time.sleep(1)

# Global variables
new_line = '\n'
tab = '\t'

scores = array.array('i', [0, 0, 0])                            # Keeps track of each game's number of tries (an array for storing the scores # of each game)


def get_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)                               # Returns a random integer between 1 and 100


def get_guess():
    """The player guesses a number. If it is not between 1 and 100, they should be prompted again until they give a number in the correct range. """
    guess = -1                                                  # Declaring a variable named guess equal to -1
    while (guess < 1 or guess > 100):                           # While guess is less than 1 or greater than 100
        guess = int(
            input('Enter a guess number between 1 and 100: '))  # Prompt the player for a number between 1 and 100
    return guess                                                # Returns guess variable


def play_game():
    """Play three games of guessing the correct number"""

    for i in range(len(scores)):                  # Repeat until three games have been completed (Iterate through each game)

        print(f'Game Title {i + 1}: {new_line}')  # Prints game title

        computer_number = get_number()            # Generates a number for the computer  (Declaring a variable named computer_number equal to the return value of get_number)

        # Player guess
        player_guess = get_guess()                # Declaring a variable named player_guess equal to the return value of get_guess
        number_of_tries = 1                       # Declaring a variable named number_of_tries equal to 1

        while (True):                             # Creates an infinite loop, will be broken when player guesses correctly (Keeping track of the number of tries)

            if (player_guess < computer_number):        # If player_guess is less than computer_number
                print(f'guess is too low {new_line}')   # Print that the guess is too low and prompts player to make another guess
                player_guess = get_guess()              # Re-assign player_guess to the return value of get_guess

                number_of_tries += 1                    # Increments the numnber of tries by 1

            elif (player_guess > computer_number):      # If player_guess is greater than computer_number
                print(f'guess is too high {new_line}')  # Print that the guess is high low and prompts player to make another guess
                player_guess = get_guess()              # Re-assign player_guess to the return value of get_guess

                number_of_tries += 1                    # Increments the number of tries by 1

            else:
                # If the player's guess is correct, congratulate them and print the number of tries it took to get the answer right

                print(f' {new_line}{new_line}')
                print(f'Congratulations, you got it right!')
                print(f'It took you {number_of_tries} tries it took to get the answer.')

                scores[i] = number_of_tries     # Store the number of tries in the scores array
                number_of_tries = 1             # Reset the number of tries to 1
                break                           # Break out of the loop

    print(f'Well, goodbye and good luck! {new_line}{new_line}')


def print_scores():
    """Prints the individual game scores followed by the average score for the three games"""

    for score in scores:                                   # Print 3 rows of scores, one for each game (For each score in the scores array)
        game_number = 1                                    # Set game number equal to one
        print(f'\n\nGame {game_number}: {score} guesses')  # Prints the score for the game
        game_number += 1                                   # Increments the number of times game has been played by 1

    cumulative_score = 0                                   # Initializes the cumulative score to 0 (Calculate the average score)
    for score in scores:                                   # For each score in the scores array
        cumulative_score += score                          # Adds the score to the cumulative score
    average_score = (cumulative_score / len(scores))       # Calculates the average score by dividing the cumulative score by the number of games

    print(f'Your average score is: {average_score}')       # Prints the average score


def main():
    delprint("Hi there! This is a guessing game where you have to guess\n\na random number generated by me.\n\n")
    delprint("Please enter a number between 1 and 100, and I'll tell you\n\nwhether the guess is too high or too low.\n\nAfter you complete all three rounds of the game, your total score will be displayed\n\nas well as the average score for the three games.\n\n")
    delprint("Please enjoy!\n\n")
    clear()
    play_game()     # Calls the play_game() function
    print_scores()  # Calls the print_scores() function


if __name__ == "__main__":
    main()

