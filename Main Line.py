playing = True
import random

# Function that sets up word categories with their corresponding words and linking phrases
def setup_word_categories():
    word_categories = []
    
    #Define all the word categories
    musical_sections_category = {
        'category_name': 'Musical Sections',
        'words': ['Brass', 'Rythym', 'Strings', 'Wind']
    }

    party_pooper_category = {
        'category_name': 'Party Pooper',
        'words': ['Bore', 'Drag', 'Drip', 'Dud']
    }

    something_cast_category = {
        'category_name': '---Cast',
        'words': ['Pod', 'Type', 'Fore', 'Broad']
    }

    vegetable_homophones_category = {
        'category_name': 'Vegetable Homophones',
        'words': ['Charred', 'Beat', 'Leak', 'Pee']
    }

    big_of_liquid_category = {
        'category_name': 'Bit of liquid',
        'words': ['Tear', 'Drop', 'Glob', 'Bead']
    }

    pursue_category = {
        'category_name': 'Pursue',
        'words': ['Hunt', 'Stalk', 'Track', 'Trail']
    }

    eat_a_little_category = {
        'category_name': 'Eat a little',
        'words': ['Graze', 'Nibble', 'Peck', 'Snack']
    }

    ministrone_category = {
        'category_name': 'Ingredients in minestrone',
        'words': ['Beans', 'Pasta', 'Stock', 'Vegetables']
    }

    basic_tastes_category = {
        'category_name': 'Basic tastes',
        'words': ['Bitter', 'Salty', 'Sour', 'Sweet']
    }

    stand_up_to_category = {
        'category_name': 'Stand up to',
        'words': ['Brave', 'Confront', 'Face', 'Meet']
    }

    ilk_category = {
        'category_name': 'Ilk',
        'words': ['Kind', 'Sort', 'Type', 'Variety']
    }

    ism_movements_category = {
        'category_name': 'Art movements with -ism',
        'words': ['Manner', 'Expression', 'Romantic', 'Surreal']
    }


    # Append the word categories to the list
    word_categories.append(musical_sections_category)
    word_categories.append(party_pooper_category)
    word_categories.append(something_cast_category)
    word_categories.append(vegetable_homophones_category)
    word_categories.append(big_of_liquid_category)
    word_categories.append(pursue_category)
    word_categories.append(eat_a_little_category)
    word_categories.append(ministrone_category)
    word_categories.append(basic_tastes_category)
    word_categories.append(stand_up_to_category)
    word_categories.append(ilk_category)
    word_categories.append(ism_movements_category)

    return word_categories

print("Hello, and welcome to Connections for Python!")
print("It functions in practically the same way as connections does.")
print("You can have a look at the read me for the rules.")

# Function that generates a grid of words based on the categories that get selected and the grid size
def generate_grid(selected_categories, grid_size):
    all_words = []
    for category in selected_categories:
        all_words.extend(category['words'])

# Shuffles the list of all 16 randomly selected words
    random.shuffle(all_words)

    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            word = all_words[i * grid_size + j]
            row.append(word)
        grid.append(row)
    return grid

# Function that displays the game grid
def display_game(grid):
    # Print a horizontal line to visually separate the grid
    print((len(grid) * 15) * "-")

    # Iterate through each row in the grid
    for row in grid:
        # Iterate through each word in the current row
        for word in row:
            # Print the word centered within a cell with a fixed width, surrounded by "|"
            print(f"| {word.center(12)} ", end='')
        # End the row with a "|" and move to the next line
        print("| ")
        
        # Print another horizontal line to visually separate the rows
        print((len(grid) * 15) * "-")

# Function that checks if the guesses are correct
def check_guess(guesses, selected_categories):
    # Convert all words and their corresponding categories to lowercase for case-insensitive comparison
    word_to_category = {word.lower(): category['category_name'].lower() for category in selected_categories for word in category['words']}

    # Convert user guesses to lowercase
    user_guesses_lower = [guess.lower() for guess in guesses]

    # Check if all guessed words exist and belong to the same category
    guessed_categories = set(word_to_category.get(guess, None) for guess in user_guesses_lower)
    if None in guessed_categories:
        print("One or more guessed words do not exist.")
        return False
    if len(guessed_categories) > 1:
        print("Some are wrong.")
        return False

    print("All guesses are correct!")
    return True

# Main game loop
word_categories = setup_word_categories()
selected_categories = random.sample(word_categories, 4)
grid = generate_grid(selected_categories, 4)

# Main game loop
while playing:
    word_categories = setup_word_categories()
    selected_categories = random.sample(word_categories, 4)
    grid = generate_grid(selected_categories, 4)

    # Initialize game variables
    correct_guesses = set((word, category['category_name']) for category in selected_categories for word in category['words'])
    lives = 4
    incorrect_guesses = set()

    # Start the loop for each round of the game until the player runs out of lives
    while lives > 0:
        # Display the game grid for the player
        display_game(grid)

        # Prompt the player to enter their guesses separated by spaces and split the input into a list
        user_input = input("Enter your guesses separated by spaces AND with capital letters: ").split()

        # Check if the number of guesses entered by the player is not exactly four
        if len(user_input) != 4:
            print("Please enter exactly four guesses.")
            continue # Skip to the next iteration of the loop if the condition is met

        new_guess = frozenset(user_input)  # Convert the guesses to frozenset for immutability

        # Check if the new guess has already been correctly guessed
        if new_guess in correct_guesses:
            print("You have already guessed this set correctly.")
            continue

        # Check if the new guess has already been entered before as an incorrect guess
        if new_guess in incorrect_guesses:
            print("You have already entered these guesses before.")
            lives -= 1 # Decrease the player's remaining lives
            print(f"You have {lives} lives left.")
            continue

        # Check if all guesses are correct by calling the check_guess function
        if check_guess(user_input, selected_categories):
            print("All guesses are correct!")

            # Add the correct guesses to the set of correct guesses
            correct_guesses.add((word, category['category_name']) for category in selected_categories for word in user_input)

            if len(correct_guesses) == 4:  # Check if all sets have been correctly guessed
                print("Congratulations! You've guessed all sets correctly!")
                # Print a message based on the remaining lives
                if lives == 4:
                    print("That was sublime.")
                elif lives == 3:
                    print("That was great.")
                elif lives == 2:
                    print("That was pretty good.")
                elif lives == 1:
                    print("That was close.")

                # Exit the inner loop as the game is won
                break
            # Print the correctly guessed set and its linking word
            for category in selected_categories:
                if set(user_input) == set(category['words']):
                    print(f"Correctly guessed set: {user_input}")
                    print(f"Linking phrase: {category['category_name']}")
                    break
        else:
            lives -= 1
            print(f"Incorrect guesses. You have {lives} lives left.")
            incorrect_guesses.add(new_guess)  # Add the incorrect guess to the set of incorrect guesses

        if lives == 0:
            print("You've run out of lives. Game over.")
            break
    
    # Ask the player if they want to play again and convert their input to lowercase
    play_again = input("Do you want to play again? (yes/no): ").lower()

    # Handling invalid input for playing again
    # Validate the user input to ensure it's either 'yes' or 'no'
    while play_again not in ['yes', 'no']:
        # If the input is not valid, prompt the user to enter 'yes' or 'no' and take input again
        print("Please enter 'yes' to play again or 'no' to quit.")
        play_again = input("Do you want to play again? (yes/no): ").lower()

    # If the player chooses to play again ('yes'), restart the game loop
    if play_again == "yes":
        continue
    # If the player chooses not to play again ('no'), print a thank you message and break out of the loop
    elif play_again == "no":
        print("Thank you for playing!")
        break