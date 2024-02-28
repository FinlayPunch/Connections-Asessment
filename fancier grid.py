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

    word_categories.append(musical_sections_category)
    word_categories.append(party_pooper_category)
    word_categories.append(something_cast_category)
    word_categories.append(vegetable_homophones_category)


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
    print((grid_size*4+19)*"-")

    # Other rows
    for i in range(grid_size):
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            print(f"| {word_categories} ", end='')
        print("| ")
        print((grid_size*4+19)*"-")


display_game(word_categories[0]["words"][random.randint(0,3)], 4)





# print_words_from_categories(word_categories)