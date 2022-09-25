import random
from colorama import Fore, Back, Style

print(Fore.BLUE + "====================RULES====================\n"
      "The game \"Guess the number\" has difficulty\n"
      "LEVELS, from which depends the size of the\n"
      "range in which you have to guess the number.\n"
      "Level 1 is to 100, Level 2 is to 200 and etc.\n"
      "You have 10 attempts to guess the number.\n"
      "=============================================")

while True:  # Main Program

    while True:  # Check correct input
        level = input(Fore.RESET + "Choose LEVEL: ")
        if level.isdigit():
            if level != "0":
                break
            else:
                print(Fore.RED + "Invalid input. Try again...")
        else:
            print(Fore.RED + "Invalid input. Try again...")

    if_not_win = True
    attemps = 10
    computer_number = random.randint(1, 100 * int(level))

    while attemps > 0:  # The Game

        print(Fore.RESET + f"You have {attemps} attemps left")
        print(Fore.BLUE + "=============================================")
        player_input = input(Fore.RESET + f"Guess the number (1-{100 * int(level)}): ")

        if not player_input.isdigit():
            print(Fore.RED + "Invalid input. Tru again...")
            continue

        player_number = int(player_input)

        if player_number == computer_number:
            print(Fore.YELLOW + "You guess it!")
            print(Fore.BLUE + "===================YOU WON===================")
            if_not_win = False
            break
        elif player_number > computer_number:
            print(Fore.RED + "High!")
        else:
            print(Fore.CYAN + "Low!")

        attemps -= 1

    if if_not_win:
        print(Fore.RED + "==================YOU LOST!==================")

    while True:  # Check for restart

        new_game_ask = input(Fore.BLUE + "Do you want new game? (y/n): ")

        if new_game_ask in ("y", "n"):
            break

        print(Fore.RED + "Invalid input. Try again...")

    if new_game_ask == "y":
        attemps = 10
        continue
    else:
        print(Fore.BLUE + "\n"
                          "                 * GOODBYE *")
        break
