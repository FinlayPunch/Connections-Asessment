import os

playing = True
lives = 4

correctguesses = {'words': ['bore', 'drag', 'drip', 'dud']}

while playing:
    guesses = input("Enter your guesses separated by spaces: ").split()
    if len(guesses) != 4:
        print("Please enter exactly four guesses.")
        continue

    # Sort both the user's guesses and the correct guesses
    sorted_guesses = sorted(guesses)
    sorted_correct_guesses = sorted(correctguesses['words'])

    new_guesses = " - ".join([f"Guess {i}: {guess}" for i, guess in enumerate(sorted_guesses, start=1)])
    try:
        with open('user_data.txt', 'r') as file:
            content = file.read()
            if new_guesses in content:
                print("You have already entered these guesses")
            else:
                with open('user_data.txt', 'a') as file:
                    file.write(new_guesses + '\n')
                print("Guesses added")
    except FileNotFoundError:
        with open('user_data.txt', 'w') as file:
            file.write(new_guesses + '\n')
        print("Guesses added")
    print(new_guesses)

    correct = True
    for guess, correct_guess in zip(sorted_guesses, sorted_correct_guesses):
        if guess.lower() != correct_guess.lower():
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