from collections import defaultdict


grid = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
with open("input.txt") as f:
    for line in f: grid.append(line.strip()) 

visited = dict()

def dfs(i, j):
    end_points = set()
    if grid[i][j] == '9': 
        end_points.add((i, j))
    elif (i, j) in visited:
        end_points = visited[(i, j)]
    else:
        for (x, y) in directions: 
            if i + x in range(n) and j + y in range(m) and int(grid[i + x][j + y]) == int(grid[i][j]) + 1:
                temp = dfs(i + x, j + y)
                for end_point in temp: end_points.add(end_point)

        visited[(i, j)] = end_points 

    return end_points 
            


n, m = len(grid), len(grid[0])
ans = 0                              
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            end_points = dfs(i, j)
            score = len(end_points)
            ans += score

print(ans)


