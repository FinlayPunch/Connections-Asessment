
import random

with open('Words.txt', "r") as f:#opens the text file
    words = f.read().split()
    random.shuffle(words)#shuffles the words in the grid
    replacement = words[0]
    removed = words[1]
    words.remove(replacement)

grid = [words[i:i + 4] for i in range(0, len(words), 4)]
r = len(words)%4

if r==0:
    for x,y,z,k in grid:
        print(x,y,z,k) #displays grid
else:
    grid = grid[: -1]
    for x,y,z,k in grid:
        print(x,y,z,k) #displays grid
