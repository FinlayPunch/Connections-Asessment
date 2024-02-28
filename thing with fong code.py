import random
from random import randint

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

connections = [
{"Connecting Word": "Vegetable Homphones", "Words": ['Charred', 'Beat', 'Leak', 'Pee']},
{"Connecting Word": "Party Pooper", "Words": ['Drag', 'Drip', 'Drip', 'Dud']},
{"Connecting Word": "---Cast", "Words": ['Pod', 'Broad', 'Fore', 'Type']},
{"Connecting Word": "Musical Sections", "Words": ['Brass', 'String', 'Rythym', 'Wind']},
]

grid = [
["word", "word", "word", "word"],
["word", "word", "word", "word"],
["word", "word", "word", "word"],
["word", "word", "word", "word"],
]

row = 0
for connection in connections: #for each of the connections, access the dictionary
    col = 0
    for word in connection["Words"]: #within dictionary, get word
        #put the word inside the correct GR
        grid[row][col] = (word)
        col = col + 1 #moves to the column
    row = row + 1 #moves to next row

print(grid)

# print(random.choice(grid))
# print(random.choice(grid))
# print(random.choice(grid))
# print(random.choice(grid))




# print_words_from_categories(word_categories)