"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

import random


def get_integer_input(prompt):
    """Get an integer input from the user and handle non-integer inputs."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The game allows for a specified lower and upper bound for guessing.
    It handles non-integer inputs, numbers outside the bounds, and other failure modes.
    """

    print("Welcome to the Advanced Guessing Game!")
    lower_bound = get_integer_input("Enter the lower bound: ")
    upper_bound = get_integer_input("Enter the upper bound: ")
    
    # Validate bounds
    if lower_bound >= upper_bound:
        print("Invalid bounds. The lower bound must be smaller than the upper bound.")
        return

    # Generate a random number within the specified range
    secret_number = random.randint(lower_bound, upper_bound)
    
    while True:
        guess = get_integer_input(f"Guess a number between {lower_bound} and {upper_bound}: ")
        
        if guess < lower_bound or guess > upper_bound:
            print("Out of bounds! Guess within the specified range.")
            continue
        
        if guess == secret_number:
            return "You got it!"
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


if __name__ == "__main__":
    print(advancedGuessingGame())
"You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
