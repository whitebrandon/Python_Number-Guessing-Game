import random
import sys

## sys.exit("Too many invalid password attempts) ← To exit loop


def start_game():
	player_name = input("Welcome to the Random Number Guessing game. Please enter your name. ");
	player_guess = ""
	solution = random.randint(0, 10)
	print("Hi, {}".format(player_name))
	guess_count = 1
	while player_guess != solution:
		try:
			while player_guess is not int:
				try:
					player_guess = int(input("Please select a number between 1 and 10. "))
				except ValueError:
					print("Oh no! That's not a valid value. Try again...")
				if player_guess > solution:
					player_guess = int(input("It's lower. "))
					guess_count += 1
				elif player_guess < solution:
					player_guess = int(input("It's higher. "))
					guess_count += 1
		except ValueError:
			print("Oh no! That's not a valid value. Try again...")
			
	print("You got it right! Congrats! It took you {} guesses to find the number".format(guess_count))


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()