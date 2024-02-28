def display_game(game, grid_size):
    c = 65

    # First row
    print(f"  ", end='')
    for j in range(grid_size):
        print(f"| {j+1} ", end='')
    print("| ")
    print((grid_size*4+4)*"-")

    # Other rows
    for i in range(grid_size):
        print(f"{chr(c+i)} ", end='')
        for j in range(grid_size):
            print(f"| {game} ", end='')
        print("| ")
        print((grid_size*4+4)*"-")


display_game('~', 4)