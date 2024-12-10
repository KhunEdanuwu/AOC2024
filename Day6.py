with open("input/Day6.txt") as f:
    lines = f.read().splitlines()

grid = [[x for x in i] for i in lines]
for row in grid:
    print(row)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        # print(f"{x} -- {y}")
        if grid[y][x] == '^':
            start_point = (y,x)

print(start_point)

# On prends le point et on fait une substring sur la direction jusqu'a un obstacle
# on enregistre les pos passée si pas déja enregistré
# On change le starting point 
# On rotate de 90 degré 
# Rebelotte jusque ... (pos == bordure) => substring n'a pas d'obstacle on compte all et done
# On compte le nombre de pos passée

dir_order = [(-1,0), (0,1), (-1,0), (0,-1)]
curr_dir_ind = 0
in_border = False 
while not in_border:
    if curr_dir_ind == 'U':
        # deplacement = [[grid[start_point][xx] for xx in x] for x in range(start_point[0], 0, -1)]
        deplacement = []
        for x in range(start_point[0], 0, -1):
            deplacement.append(grid[start_point[1]][x])
        print(deplacement)
        curr_dir_ind = (1 % 4) + 1
    # elif curr_dir_ind == 'R': 
    #     pass
    # elif curr_dir_ind == 'D':
    #     pass
    # elif curr_dir_ind == 'L':
    #     pass
