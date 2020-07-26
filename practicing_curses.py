import curses
import time
import csv
from banner import banner

menu = ['About', 'Play Game', 'High Scores', 'Exit']

def print_banner(stdscr, dictionary):
    height, width = stdscr.getmaxyx()
    banner_len = len(dictionary) if height // 2 > len(dictionary) else height // 2
    for i, row in enumerate(dictionary.values()):
        x = width // 2 - row[0] // 2
        y = height // 2 - banner_len + i
        stdscr.addstr(y, x, row[1])
    stdscr.addstr(banner_len + 5, width // 2 - len("Press any key to continue") // 2, "Press any key to continue")
    stdscr.refresh()

def print_menu(stdscr, selected_row_index):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    for i, row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) + i
        if i == selected_row_index:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()

def main(stdscr):
    height, width = stdscr.getmaxyx()
    player = {"name": None, "score": 0}
    curses.curs_set(0) # disables cursor blinking
    print_banner(stdscr, banner)
    stdscr.getch()
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0
    print_menu(stdscr, current_row_idx)

    while True:
        key = stdscr.getch()

        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, f"You pressed {menu[current_row_idx]}")
            if menu[current_row_idx] == "About":
                stdscr.clear()
                about = ["About", "Try to guess the number"]
                for i, sentence in enumerate(about):
                    stdscr.addstr(height // 2 + i, width // 2 - len(sentence) // 2, sentence)
                    stdscr.refresh()
                stdscr.getch()
            elif menu[current_row_idx] == "Play Game":
                while True:
                    curses.curs_set(1)
                    curses.echo()
                    stdscr.clear()
                    stdscr.addstr(10, width // 2 - len("Let's get started. Please enter your name to continue. ") // 2, "Let's get started. Please enter your name to continue.\n")
                    player_name = stdscr.getch(11, width // 2)
                    current_player = []
                    i = 1
                    while True:
                        current_player.append(chr(player_name))
                        player_name = stdscr.getch(11, width // 2 + i)
                        if player_name == curses.KEY_ENTER or player_name in [10, 13]:
                            break
                        i += 1
                    player["name"] = "".join(current_player)
                    stdscr.refresh()
                    curses.napms(5000)
                    end_game = True
                    break
                if end_game:
                    with open('scores.csv', 'a') as file:
                        writer = csv.DictWriter(file, ["name, score"])
                        if player["name"]:
                            writer.writerow(player)
                    break
                    #     player_guess = None
                    #     # 2. Store a random number as the answer/solution
                    #     solution = random.randint(MIN_NUM, MAX_NUM)
                    #     print("Hi, {}. Let's begin.".format(player_name))
                    #     guess_count = 1
                    #     # 3. Continuously prompt the player for a guess.
                    # #     a. If the guess greater than the solution, display to the player "It's lower".
                    # #     b. If the guess is less than the solution, display to the player "It's higher".
                    #     while player_guess != solution:
                    #         if not isinstance(player_guess, int):
                    #             try:
                    #                 player_guess = int(input("First select a number between 1 and 10.\n"))
                    #                 if player_guess < MIN_NUM or player_guess > MAX_NUM:
                    #                     raise ValueError("Don't forget, it's MORE than {}, but LESS than {}".format(MIN_NUM - 1, MAX_NUM + 1))
                    #             except ValueError as error:
                    #                 print("Oops, that value won't work. Please try it again...")
                    #                 if isinstance(player_guess, int):
                    #                     print("({})".format(error))
                    #                 continue
                    #         else:
                    #             try:	
                    #                 if player_guess > solution:
                    #                     player_guess = int(input("It's lower.\n"))
                    #                     guess_count += 1
                    #                 elif player_guess < solution:
                    #                     player_guess = int(input("It's higher.\n"))
                    #                     guess_count += 1
                    #             except ValueError:
                    #                 if not isinstance(player_guess, int):
                    #                     continue
                    #                 else:
                    #                     print("Oh no! That's not a valid value. Try again...")
                    #             except TypeError:
                    #                 print("Guess should be a whole number. Please try again...")
                    #     # 4. Once the guess is correct, stop looping, inform the user they "Got it"
                    # #        and show how many attempts it took them to get the correct number.
                    #     print("You got it right! Congrats! It took you {} guesses to find the number".format(guess_count))
        # else:
        #     with open('scores.csv', 'a') as file:
        #         print(player)
        #         writer = csv.DictWriter(file, ["name, score"])
        #         if player["name"]:
        #             writer.writerow(player)

        #     break
        
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()

    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_YELLOW) # initializes fg color and bg color, but doesn't activate it | sets id to 1


    # height, width = stdscr.getmaxyx()

    # text = "Hello, World!"

    # x = width // 2 - len(text) // 2
    # y = height // 2

    # stdscr.attron(curses.color_pair(1))
    # stdscr.addstr(y, x, text)
    # stdscr.attroff(curses.color_pair(1))

    # stdscr.refresh()

    # time.sleep(3)

    # stdscr.addstr(5, 5, ascii_banner)
    # stdscr.refresh()
    # time.sleep(3)

curses.wrapper(main)