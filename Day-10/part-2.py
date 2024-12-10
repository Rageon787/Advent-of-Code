from collections import defaultdict


grid = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
with open("sample.txt") as f:
    for line in f: grid.append(line.strip()) 

visited = dict()

def dfs(i, j):
    rating = 0 
    if grid[i][j] == '9': 
        rating += 1
    elif (i, j) in visited:
        rating = visited[(i, j)]
    else:
        for (x, y) in directions: 
            if i + x in range(n) and j + y in range(m) and int(grid[i + x][j + y]) == int(grid[i][j]) + 1:
                rating += dfs(i + x, j + y)

        visited[(i, j)] = rating 

    return rating 
            


n, m = len(grid), len(grid[0])
ans = 0                              
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            rating = dfs(i, j)
            ans += rating

print(ans)


