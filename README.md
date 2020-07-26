# Description
## Short Description (used on project cards, visible to students even if unpublished)
Build a console number guessing game that prompts a player to choose a number between a specified range of numbers. After the user guesses the correct number, display the number of attempts it took them to guess correctly.

## Long Description (used on details page)
In this project you will build a console game that will let you exercise the skills and concepts you have learned in the unit so far. This game is often called the Number Guessing Game or the Pick A Number game.

Have you ever played a game with your friends where you ask them to pick a number between some range of numbers like: "Pick a number between 1 and 10". Their job is to make a guess, and you tell them whether their guess is too high or too low. Their next guess is based on what you've told them. If they guess the right answer the game is done. Normally you try to do this in the lowest number of tries possible. Often it is used to compete with friends to see who can get the answer in the lowest number of guesses.

To complete each part of this project, use ONLY the concepts and techniques we have covered in the courses so far.

2.0 hours to complete

```
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()
```

Instructions
This is how instructions will be displayed:

Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
For example, non-number guesses should be handled with an exception.

As a player of the game, I should see a some kind of text header, welcome or game intro message.
A random number should be chosen that is within the range.
As a player of the game, I should be continuously prompted for a guess until I get it right.
As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses.
As a player of the game, after the game ends I should be shown my number of attempts at guessing.
When the game ends, an ending message is shown to the player.
Before you submit your project for review, make sure you can check off all of the items on the Student Project Submission Checklist. The checklist is designed to help you make sure you’ve met the grading requirements and that your project is complete and ready to be submitted!
Extra Credit
This is how Extra Credit will be displayed:

As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
For example, if the range is 1-10 and the player enters 12 they should be informed that this number is outside the range.

As a player of the game, after I guess correctly I should be prompted if I would like to play again.
As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.

***

Requirement: Run Script
Highest Grade: Meets Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
Program crashes at any point due to an uncaught exception.
Program runs, any exceptions are caught and handled, preventing crashes while its running.
N/A

Feedback Template
Uh oh! It looks like your script crashes with an exception.

Feedback Template
Great work making sure your program doesn't crash during usage.

Notes
None

Requirement: Display Intro
Highest Grade: Meets Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
Program does not show an initial intro/welcome message when run.
When run, the program displays an initial intro/welcome message before or above the menu.
N/A

Feedback Template
Oops! Looks like you forgot to add an initial welcome message when your program is first run.

Feedback Template
Great, I was shown an intro/welcome message when the game launched.

Notes
None

Requirement: Random Number
Highest Grade: Exceeds Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
The number to guess was not a random number within the range.

When run, a random number within the range is chosen for the player to guess.

When the player chooses to play the game again, a new random number within the range is chosen each time.

Feedback Template
Oops! Looks like you forgot to choose a random number within the range for the number to guess.

Feedback Template
Nice work! The player has to guess a random number.

Feedback Template
Nice work! You were able to change the number so each time the player decides to play again, they get to guess a new number.

Notes
None

Requirement: User input
Highest Grade: Exceeds Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
The player was not prompted for their number choice.
The player is prompted for a number guess, non-numbers were handled by exception catching.
The player cannot enter a number that is outside the number range. If the player tries they are informed that number was not a valid option and to try again.
Feedback Template
Oops! I was not prompted for a number input as my guess.

Feedback Template
I was able to successfully pass a number and passing non-numbers did not break the program.

Feedback Template
Great work! Not only did you validate that it was a number, but you also made sure that the player was within the proper range.

Notes
None

Requirement: Responding to the player
Highest Grade: Meets Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
The player is not given feedback after each guess, of whether they need to guess higher or lower.
The player receives the correct feedback for their choice:

If the solution is higher than the guess, display "It's higher".
If the solution is lower than the player's guess, display "It's lower"
N/A

Feedback Template
Oops! I was not informed to guess higher or lower based on my guess.

Feedback Template
Nice! Each time I make an incorrect guess the program displays a hint to guess higher or lower.

Notes
None

Requirement: Displaying Tries
Highest Grade: Exceeds Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
The player was not shown how many attempts they made at the end of each game.
The player is shown their number of tries at the end of each game once they have guessed the correct number.
Display a high score (number of least guesses) at the start of a new game so the player knows the goal they are trying to beat.
Feedback Template
After the game ends, the number of attempts I made was not shown to me.

Feedback Template
Nicely done! Each time the game ends the program shows me how many attempts I made.

Feedback Template
Amazing! You created a way for the user to see the high score at the start of or during their game.

Notes
None

Requirement: Display End Game
Highest Grade: Exceeds Expectations

NEEDS WORK	MEETS EXPECTATIONS	EXCEEDS EXPECTATIONS
When the game ends, the program did not show a quit/closing message.

The player is shown an ending/quit/goodbye message when the game ends.

Instead of just ending the game each time, ask the user if they would like to play again.
If yes, then cycle the user back into guessing a number again.
If no, then provide the user with an ending/quit/goodbye message.
Feedback Template
Uh oh, it looks like your program did not display anything to the user when quitting the game to let them know the game was closing.

Feedback Template
Nice work! User experience is important in console applications, especially terminal games. Giving plenty of feedback to the user lets them understand whats going on and make decisions.

Feedback Template
Awesome! Now the player can keep playing as long as they want without having to stop/start the script!

