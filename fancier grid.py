import random

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
    
    #This is the top set of dashes
    print((grid_size*4+27)*"-")

    #These are the row that contain the words
    for i in range(grid_size):
        for j in range(grid_size):
            random_word = word_categories[random.randint(0, len(word_categories) - 1)]["words"][random.randint(0, 3)] #random word = a random word from a random category from word categories
            print(f"| {random_word:8} ", end='')  # adjusts the width to match the longest word
        print("| ")
        print((grid_size*4+27)*"-")


display_game(word_categories, 4)





# print_words_from_categories(word_categories)