playing = True
lives = 4
correct_guesses = 0  # Track the number of correctly guessed groups
import random
import os

def print_words_from_categories(word_categories):
    for category in word_categories:
        for word in category['words']:
            print(word)

def setup_word_categories():
    word_categories = []
    
    musical_sections_category = {
        'category_name': 'Musical Sections',
        'gen_num': 1,
        'words': ['Brass', 'Rythym', 'Strings', 'Wind']
    }

    party_pooper_category = {
        'category_name': 'Party Pooper',
        'gen_num': 2,
        'words': ['Bore', 'Drag', 'Drip', 'Dud']
    }

    something_cast_category = {
        'category_name': '---Cast',
        'gen_num': 3,
        'words': ['Pod', 'Type', 'Fore', 'Broad']
    }

    vegetable_homophones_category = {
        'category_name': 'Vegetable Homophones',
        'gen_num': 4,
        'words': ['Charred', 'Beat', 'Leak', 'Pee']
    }

    big_of_liquid_category = {
        'category_name': 'Bit of liquid',
        'gen_num': 5,
        'words': ['Tear', 'Drop', 'Glob', 'Bead']
    }

    pursue_category = {
        'category_name': 'Pursue',
        'gen_num': 6,
        'words': ['Hunt', 'Stalk', 'Track', 'Trail']
    }

    eat_a_little_category = {
        'category_name': 'Eat a little',
        'gen_num': 7,
        'words': ['Graze', 'Nibble', 'Peck', 'Snack']
    }

    ministrone_category = {
        'category_name': 'Ingredients in minestrone',
        'gen_num': 8,
        'words': ['Beans', 'Pasta', 'Stock', 'Vegetables']
    }

    basic_tastes_category = {
        'category_name': 'Basic tastes',
        'gen_num': 9,
        'words': ['Bitter', 'Salty', 'Sour', 'Sweet']
    }

    stand_up_to_category = {
        'category_name': 'Stand up to',
        'gen_num': 10,
        'words': ['Brave', 'Confront', 'Face', 'Meet']
    }

    ilk_category = {
        'category_name': 'Ilk',
        'gen_num': 11,
        'words': ['Kind', 'Sort', 'Type', 'Variety']
    }

    ism_movements_category = {
        'category_name': 'Art movements with -ism',
        'gen_num': 12,
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
    # Extract all words and their corresponding categories from the selected categories
    word_to_category = {word.lower(): category['category_name'] for category in selected_categories for word in category['words']}

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

def save_guesses_to_file(guesses):
    try:
        with open('user_data.txt', 'a') as file:
            file.write(' '.join(guesses) + '\n')
    except FileNotFoundError:
        with open('user_data.txt', 'w') as file:
            file.write(' '.join(guesses) + '\n')

# Main game loop
word_categories = setup_word_categories()
selected_categories = random.sample(word_categories, 4)
grid = generate_grid(selected_categories, 4)

while lives > 0:
    display_game(grid)
    user_input = input("Enter your guesses separated by spaces: ").split()
    if len(user_input) != 4:
        print("Please enter exactly four guesses.")
        continue

    if check_guess(user_input, selected_categories):
        print("Your guesses are correct!")
        correct_guesses += 1
        if correct_guesses == 4:  # Check if all groups have been correctly guessed
            print("Congratulations! You've guessed all groups correctly!")
            break
    else:
        lives -= 1
        print(f"Incorrect guesses. You have {lives} lives left.")

        if lives == 0:
            print("You've run out of lives. Game over.")
            break

# Remove the file after the player decides to quit the game
if os.path.exists('user_data.txt'):
    os.remove('user_data.txt')