import random
from time import sleep
from colorama import Fore

rules_for_print = """The game "Guess the number" has difficulty
LEVELS, from which depends the size of the
range in which you have to guess the number.
Level 1 is to 100, Level 2 is to 200 and etc.
You have 10 attempts to guess the number."""

print(Fore.BLUE + "====================RULES====================")
i = 0
while i < len(rules_for_print):  # Print character by character
    sleep(0.001)
    print(Fore.BLUE + rules_for_print[i] + Fore.RESET, end='')
    i += 1
print()
print(Fore.BLUE + "n=============================================" + Fore.RESET)

while True:  # Main Program

    while True:  # Check correct input
        level = input("Choose LEVEL: ")
        if level.isdigit():
            if level != "0":
                break
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

        if player_number == 0 or player_number > (int(level) * 100):
            print(Fore.RED + "Out of range! Tru again...")
            continue

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
        print(Fore.RED + f"The Number was: {computer_number}")
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
