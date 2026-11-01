from random import randrange

'''
Generate a random number from a range of 0 to 10
To adjust the range edit the values within the parentheses ()
The first number controls the lower bounds and the second controls the higher bounds
'''


while True:
#define guess variable, user attempts and max credits (tries)
    random_number = randrange(0, 10)
    guess = None
    attempts = 0
    credits = 5

# get the user's input and explains what to expect.
    while credits > 0:
        guess = input(f"Guess the number between 0 and 10. You have {credits} credits: ")
        guess = int(guess)
        attempts = attempts + 1

# Loop continues until user guesses right or runs out of credits.
    
        if guess == random_number:
            print(f"Good job! You got it right!\nIt took you {attempts} guesses.")
            break
        else:
            credits = credits - 1
            if credits > 0:
                print(f"That wasn't it. You have {credits} credits left.")
            else:
                print(f"You have run out of credits! The correct number was {random_number}")

# Restart game code to validate if the user wants to restart the game.
    while True:
        restart_game = input("Alrighty then. Restart this whole shebang? (y/n): ").lower()
        if restart_game in ['y', 'yes', 'n', 'no']:
            break
        else:
            print("Invalid response, please type a y/yes or an n/no.")

    if restart_game == 'n' or restart_game == 'no':
        print("Okay, until next time!\nCreated by Daniel Brown")
        break


    
    
