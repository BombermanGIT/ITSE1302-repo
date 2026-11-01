#!/usr/bin/env python3
from random import randrange

def get_user_choice():
    # define user choice variables. Also checks against invalid inputs.
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        
        print("Invalid choice. Please enter a number.")


def get_opponent_choice():
    # Define random number for opponent.
    return randrange(1, 4)


def determine_winner(user_choice, opponent_choice):
    # This gives some flavor to the integers, and determins the winner based on rock-paper-scissors rules
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors",
    }

    user = choices[user_choice]
    opponent = choices[opponent_choice]

    if user_choice == opponent_choice:
        print("It is a draw!")
    elif user_choice == 1 and opponent_choice == 3:
        print("You win! Rock beat the Scissors!")
    elif user_choice == 2 and opponent_choice == 1:
        print("You win! Paper covers the Rock!")
    elif user_choice == 3 and opponent_choice == 2:
        print("You win! Scissors cuts the Paper!")
    elif opponent_choice == 1 and user_choice == 3:
        print("You lost! Rock beat the Scissors!")
    elif opponent_choice == 2 and user_choice == 1:
        print("You lost! Paper covers the Rock!")
    elif opponent_choice == 3 and user_choice == 2:
        print("You lost! Scissors cuts the Paper!")


def main():
    play_again = "y"
    # While loop to determin if user wants to continue
    while play_again == "y":
        print("ROCK, PAPER, SCISSORS!")
        print("Please enter a number to select Rock, Paper or Scissors!")

        user_choice = get_user_choice()
        opponent_choice = get_opponent_choice()

        determine_winner(user_choice, opponent_choice)

        while True:
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again in ("y", "n"):
                break
            print("Invalid choice. Please enter y or n.")

    print("Thank you for playing!")
    print("Completed by Daniel Brown")


if __name__ == "__main__":
    main()
