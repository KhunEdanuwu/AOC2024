with open("input/Day8.txt") as f:
    lines = f.readlines()

grid = [[x for x in line.strip()] for line in lines]

map = {}

for row in grid:
    print(row)

 

for cy in range(len(grid)):
    for cx in range(len(grid[0])):
        if grid[cy][cx] != '.':
            if (grid[cy][cx]) not in map.keys():
                map[grid[cy][cx]] = []
            map[grid[cy][cx]].append((cy,cx))

 

print(map)

 

# Pour chaque key
# Pour chaque elem
# loop sur les autres elems
# On abs(x1-x2, y1-y2) | réfléci mais selon leur postion relative
# On met les antinodes et on les saves dans la liste d'antinode


# e1(1,8) et e2(2,5)
# e1 -> e2 (+1, -3)
# e2 -> e1 (-1, +3)
# antinode se place a d(e1 -> e2)x2 et d(e2->e1)x2

 

antinodes = []
for key in map.keys():
    for elem in map[key]:
        ey, ex = elem        
        for value in map[key]:
            if value != elem:
                vy, vx = value
                dist_y, dist_x = vy - ey, vx - ex
                antinodes.append((ey + 2 * dist_y, ex + 2 * dist_x))
                antinodes.append((vy - 3 * dist_y, vx - 3 * dist_x))

cnt = 0
for z in antinodes: 
    if z[0] >= 0 and z[1] >= 0 and z[0] <=  len(grid) - 1 and z[1] <= len(grid[0]) - 1:
        cnt += 1

print(cnt)