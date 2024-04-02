playing = True
import random
import colorama



def setup_word_categories():
    word_categories = []
    
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

def generate_grid(selected_categories, grid_size):
    all_words = []
    for category in selected_categories:
        all_words.extend(category['words'])

    random.shuffle(all_words)

    grid = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            word = all_words[i * grid_size + j]
            row.append(word)
        grid.append(row)
    return grid

def display_game(grid):
    print((len(grid) * 15) * "-")
    for row in grid:
        for word in row:
            print(f"| {word.center(12)} ", end='')
        print("| ")
        print((len(grid) * 15) * "-")

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

while playing:
    word_categories = setup_word_categories()
    selected_categories = random.sample(word_categories, 4)
    grid = generate_grid(selected_categories, 4)

    correct_guesses = set((word, category['category_name']) for category in selected_categories for word in category['words'])
    lives = 4
    incorrect_guesses = set()

    while lives > 0:
        display_game(grid)
        user_input = input("Enter your guesses separated by spaces: ").split()
        if len(user_input) != 4:
            print("Please enter exactly four guesses.")
            continue

        new_guess = frozenset(user_input)  # Convert the guesses to frozenset for immutability
        if new_guess in correct_guesses:
            print("You have already guessed this set correctly.")
            continue

        if new_guess in incorrect_guesses:
            print("You have already entered these guesses before.")
            lives -= 1
            print(f"You have {lives} lives left.")
            continue

        if check_guess(user_input, selected_categories):
            print("All guesses are correct!")
            correct_guesses.add((word, category['category_name']) for category in selected_categories for word in user_input)
            if len(correct_guesses) == 4:  # Check if all sets have been correctly guessed
                print("Congratulations! You've guessed all sets correctly!")
                if lives == 4:
                    print("That was sublime.")
                elif lives == 3:
                    print("That was great.")
                elif lives == 2:
                    print("That was pretty good.")
                elif lives == 1:
                    print("That was close.")
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

    play_again = input("Do you want to play again? (yes/no): ").lower()

    while play_again not in ['yes', 'no']:
        print("Please enter 'yes' to play again or 'no' to quit.")
        play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == "yes":
        continue
    elif play_again == "no":
        print("Thank you for playing!")
        break