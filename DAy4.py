# Wrap the grid  lines = ['....' + line + '....' for line in lines]

with open("input/Day4.txt") as f:
    lines = f.read().splitlines()

grid = [['0'] + [i for i in line] + ['0'] for line in lines]

# Add top and bot wrapping to grid
grid = [['0'] * len(grid[0])] + grid + [['0'] * len(grid[0])]

for row in grid:
    print(row)

# grid[y][x]
# x = 5
# y = 1
# elem = grid[1][5]
# height = len(grid)
# width = len(grid[0])
# right_word = [grid[y][i] for i in range(x, min(x+4, width))]
# down_right_word = [grid[y+i][x+i] for i in range(4) if y+i < height and x+i < width]
# print(down_right_word)
# left_word = []
# for i in range(x, x-3, -1):
#     if i == 0:
#         break
#     left_word.append(grid[y][i])


# up_word = []
# for i in range(y, y-3, -1):
#     if i == 0:
#         up_word.append('I')
#     up_word.append(grid[i][y])
# print(up_word)

# def grid_get(grid, x, y):
#     if x < 0 or y < 0:
#         return default
#     try:
#         return grid[y][x]
#     except IndexError:
#         return default

def xmas_lookup(elem_coordonate: tuple, grid) -> int:
    nb_find = 0
    to_find = ['X', 'M', 'A', 'S']
    y, x = elem_coordonate
    height = len(grid)
    width = len(grid[0])
    left_word = [grid[y][i] for i in range(x, max(x-4, -1), -1)]
    right_word = [grid[y][i] for i in range(x, min(x+4, width))]
    up_word = [grid[i][x] for i in range(y, max(y-4, -1), -1)]
    down_word = [grid[i][x] for i in range(y, min(y+4, height))]
    up_left_word = [grid[y-i][x-i] for i in range(4) if y-i >= 0 and x-i >= 0]
    up_right_word = [grid[y-i][x+i] for i in range(4) if y-i >= 0 and x+i < width]
    down_left_word = [grid[y+i][x-i] for i in range(4) if y+i < height and x-i >= 0]
    down_right_word = [grid[y+i][x+i] for i in range(4) if y+i < height and x+i < width]    
    all_word = [left_word, right_word, up_word, down_word, up_left_word, up_right_word, down_left_word, down_right_word]
    
    for word in all_word:
        if word == to_find:
            nb_find += 1
    
    return nb_find
    

nb_xmas = 0
for y, line in enumerate(grid):
    for x, elem in enumerate(line):
        nb_find = 0
        if elem == '0':
            continue
        else:
            if elem == 'X':
                nb_find = xmas_lookup((y, x), grid)
        
        nb_xmas += nb_find
        
print(nb_xmas)
