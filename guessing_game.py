import random

print("Hi welcome to the game, This is a number guessing game.\nYou got 10 chances to guess the number. Let's start the game")

number_to_guess = random.randrange(10)

chances = 10
guess_counter = 0

while guess_counter < chances:
    try:
        my_guess = int(input('Please Enter your Guess : '))
        guess_counter += 1

        if my_guess == number_to_guess:
            print(f'The number is {number_to_guess} and you found it right !! in the {guess_counter} attempt')
            break

        elif guess_counter >= chances and my_guess != number_to_guess:
            print(f'Oops sorry, The number is {number_to_guess} better luck next time')

        elif my_guess > number_to_guess:
            print('Your guess is higher ')

        elif my_guess < number_to_guess:
            print('Your guess is lesser')

    except ValueError:
        print("Please enter a valid number.")