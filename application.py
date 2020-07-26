import random
import time
import sys

# Constants
MIN_NUM = 1
MAX_NUM = 10

# sys.exit("Too many invalid password attempts) ← To exit loop

# 1. Display an intro/welcome to the player

intro = ["YO, I'M PY THE RAPPER, HERE TO EXPLAIN...", "HOW TO PLAY THIS RANDOM NUMBER GUESSING GAME...", "HOPEFULLY IT'S FUN AND IT TESTS YOUR BRAIN...", "BUT BEFORE WE GO ON CAN I KNOW YOUR NAME?"]
def start_game():
	# for line in intro:
	# 	print(line + " "*15, end="\r")
	# 	time.sleep(2.5)
	player_name = input("Let's get started. Please enter your name to continue. ")
	player_guess = None
	# 2. Store a random number as the answer/solution
	solution = random.randint(MIN_NUM, MAX_NUM)
	print("Hi, {}. Let's begin.".format(player_name))
	guess_count = 1
	# 3. Continuously prompt the player for a guess.
  #     a. If the guess greater than the solution, display to the player "It's lower".
  #     b. If the guess is less than the solution, display to the player "It's higher".
	while player_guess != solution:
		if not isinstance(player_guess, int):
			try:
				player_guess = int(input("First select a number between 1 and 10.\n"))
				if player_guess < MIN_NUM or player_guess > MAX_NUM:
					raise ValueError("Don't forget, it's MORE than {}, but LESS than {}".format(MIN_NUM - 1, MAX_NUM + 1))
			except ValueError as error:
				print("Oops, that value won't work. Please try it again...")
				if isinstance(player_guess, int):
					print("({})".format(error))
				continue
		else:
			try:	
				if player_guess > solution:
					player_guess = int(input("It's lower.\n"))
					guess_count += 1
				elif player_guess < solution:
					player_guess = int(input("It's higher.\n"))
					guess_count += 1
			except ValueError:
				if not isinstance(player_guess, int):
					continue
				else:
					print("Oh no! That's not a valid value. Try again...")
			except TypeError:
				print("Guess should be a whole number. Please try again...")
	# 4. Once the guess is correct, stop looping, inform the user they "Got it"
  #        and show how many attempts it took them to get the correct number.
	print("You got it right! Congrats! It took you {} guesses to find the number".format(guess_count))

	# 5. Let the player know the game is ending, or something that indicates the game is over.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()