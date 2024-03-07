playing = True
GuessIsLetter = False

while playing:
    while GuessIsLetter != True:
        Guess1 = input('Guess 1: ')
        if not Guess1.isalpha():
            print("Use only letters")
        if Guess1.isalpha():
            GuessIsLetter = True
            GuessIsLetter = False
            break

    while GuessIsLetter != True:
        Guess2 = input('Guess 2: ')
        if not Guess2.isalpha():
            print("Use only letters")
        if Guess2.isalpha():
            GuessIsLetter = True
            GuessIsLetter = False
            break

    while GuessIsLetter != True:
        Guess3 = input('Guess 3: ')
        if not Guess3.isalpha():
            print("Use only letters")
        if Guess3.isalpha():
            GuessIsLetter = True
            GuessIsLetter = False
            break

    while GuessIsLetter != True:
        Guess4 = input('Guess 4: ')
        if not Guess4.isalpha():
            print("Use only letters")
        if Guess4.isalpha():
            GuessIsLetter = True
            GuessIsLetter = False
            break

   
    new_guesses = f'Guess 1: {Guess1} - Guess 2: {Guess2} - Guess 3: {Guess3} - Guess 4: {Guess4}\n'
    try:
        with open('user_data.txt', 'r') as file:
            content = file.read()
            if new_guesses in content:
                print("You have already entered these guesses.")
            else:
                with open('user_data.txt', 'a') as file:
                    file.write(new_guesses)
                print("Guesses added successfully.")
    except FileNotFoundError:
        with open('user_data.txt', 'w') as file:
            file.write(new_guesses)
        print("Guesses added successfully.")

    print("Do you want to keep going?")
    choice = input('Yes or no: ')
    if choice.lower() == 'yes':
        playing = True
    elif choice.lower() == 'no':
        playing = False
            
