import random

def print_words_from_categories(word_categories):

    for category in word_categories:
        for word in category['words']:
            print(word)

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

# def create_word_grid():

#     grid_size = 4
#     word_grid = []

#     for _ in range(grid_size):
#         row = []
#         for _ in range(grid_size):
#             row.append('words')
#         word_grid.append(row)

#     return word_grid

# word_grid = create_word_grid()
word_categories = setup_word_categories()


def display_game(word_categories, grid_size):
    c = 65

    # First row
    print(f"  ", end='')
    for j in range(grid_size):
        print(f"|   {j+1}   ", end='')
    print("| ")
    print((grid_size*4+27)*"-")

    # Other rows
    for i in range(grid_size):
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            random_word = word_categories[random.randint(0, len(word_categories) - 1)]["words"][random.randint(0, 3)] #random word = a random word from a random category from word categories
            print(f"| {random_word:7} ", end='')  # adjusts the width to match the longest word
        print("| ")
        print((grid_size*4+27)*"-")


display_game(word_categories, 4)





# print_words_from_categories(word_categories)