playing = True

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
            break

    if correct:
        print("your guesses are correct")
        print("Do you want to keep going?")
        choice = input('Yes or no: ')
        if choice.lower() == 'yes':
            playing = True
        if choice.lower() == 'no':
            playing = False
            break
    else:
        print("your guesses aren't correct")
        print("Do you want to keep going?")
        choice = input('Yes or no: ')
        if choice.lower() == 'yes':
            playing = True
        if choice.lower() == 'no':
            playing = False
            break