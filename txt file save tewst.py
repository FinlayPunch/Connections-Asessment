import os

playing = True
lives = 4

correctguesses = {
    'correctguess1': 'four',
    'correctguess2': 'five',
    'correctguess3': 'six',
    'correctguess4': 'seven',
}

while playing:
    guesses = []  
    for i in range(1, 5):
        while True:
            guess = input(f"Guess {i}: ")
            if guess.isalpha():
                guesses.append(guess)
                break
            else:
                print("Use only letters")

    new_guesses = " - ".join([f"Guess {i}: {guess}" for i, guess in enumerate(guesses, start=1)])
    try:
        with open('user_data.txt', 'r') as file:
            content = file.read()
            if new_guesses in content:
                print("You have already entered these guesses")
                
            else:
                with open('user_data.txt', 'a') as file:
                    file.write(new_guesses)
                print("Guesses added")
    except FileNotFoundError:
        with open('user_data.txt', 'w') as file:
            file.write(new_guesses)
        print("Guesses added")
    print(new_guesses)

    correct = True
    for i, guess in enumerate(guesses, start=1):
        if guess != correctguesses[f'correctguess{i}']:
            correct = False
            lives -= 1
            print(f"Incorrect guess. You have {lives} lives left.")
            if lives == 0:
                print("You've run out of lives. Game over.")
                print("Do you want to keep playing?")
                while True:
                    choice = input('Yes or no: ')
                    if choice.lower() == 'yes':
                        break  # Start the loop again for a new game
                    elif choice.lower() == 'no':
                        playing = False
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                break
            break

    if correct:
        print("Your guesses are correct")
        print("Do you want to keep playing?")
        while True:
            choice = input('Yes or no: ')
            if choice.lower() == 'yes':
                break  # Start the loop again for a new game
            elif choice.lower() == 'no':
                playing = False
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

# Remove the file after the player decides to quit the game
os.remove('user_data.txt')
