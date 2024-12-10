with open("input/Day10.txt") as f:
    lines = f.readlines()

grid = [[x for x in line.strip()] for line in lines]
width = len(grid[0])


wrapped_grid = [['.'] + row + ['.'] for row in grid]
wrapped_grid.insert(0, ['.'] * (width + 2))
wrapped_grid.append(['.'] * (width + 2))


for row in wrapped_grid:
    print(''.join(row))

moves = ((-1,0), (0,1), (1,0), (0,-1))
trailhead = set([str(i) for i in range(9)])
print(moves)

start_points = []
tt = []
for cy in range(len(wrapped_grid)):
    for cx in range(len(wrapped_grid[0])):
        #print(f"{cx}-- {cy} -- {grid[cy][cx]}")
        point = wrapped_grid[cy][cx]
        if point == '0':
            start_points.append((cy,cx))

def dfs(grid, point, visited, matching):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    my, mx = point[0], point[1]
    if grid[my][mx] == '9':
        matching[start].append((my, mx))
        return 1
    visited.append((my,mx))
    next = str(int(grid[my][mx]) + 1)
    cnt = 0
    for move in moves:
        # print(f"point({my},{mx})  --- {move} -- {next}")
        new_y, new_x = my + move[0], mx + move[1]
        if grid[new_y][new_x] in visited:
            continue
        else:
            if grid[new_y][new_x] == next:
                cnt += dfs(grid, (new_y,new_x), visited, matching)
    visited.remove((my,mx))
    return cnt

 

score = []
matching = {}
for start in start_points:
    print(start)
    visited = [start]
    matching[start] = []
    res = dfs(wrapped_grid, start, visited, matching)
    score.append(res)

print(sum(score))

rr = []
for x in matching.values():
    rr.append(len(set(x)))

print(sum(rr))