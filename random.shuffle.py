import random

example_two = {
    "Linking Word": "Hands",
    "Words": ["Nail", "Finger", "Pink", "Thumb"]
}

# Extract the words from example_two
words_to_shuffle = example_two["Words"]

# Shuffle the list of words randomly
random.shuffle(words_to_shuffle)

# Print the shuffled list
print(words_to_shuffle)