import sys 
import heapq

filename = sys.argv[1]

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

visited = dict()
def djikstra(src): 
    min_heap = [(0, src)] 
    while min_heap:  
        dist, (x, y) = heapq.heappop(min_heap) 
        if (src, x, y) in visited: continue 
        visited[(src, x, y)] = dist

        if grid[x][y] == '#': continue 

        for (dx, dy) in directions: 
            if x + dx not in range(n) or y + dy not in range(m): continue
            heapq.heappush(min_heap, (dist + 1, (x + dx, y + dy))) 

grid = []
with open(filename) as f:
    for line in f:
        grid.append(list(line.strip())) 

n, m = len(grid), len(grid[0])

print(f"{n} {m}") 
start, end = (0, 0), (0, 0)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'E' or grid[i][j] == 'S': djikstra((i, j))
        if grid[i][j] == 'S': start = (i , j) 
        if grid[i][j] == 'E': end = (i, j)
original = visited[start, end[0], end[1]]
print(original)

threshold = 100
ans = 0
for i in range(n):
    for j in range(m): 
        if grid[i][j] == '.' or grid[i][j] == 'S': 
            for (dx, dy) in directions: 
                if i + dx in range(n) and j + dy in range(m):
                    if grid[i + dx][j + dy] == '#':
                        a = visited[(start, i, j)] 
                        b = visited[(end, i + dx, j + dy)] 
                        new_dist = a + b + 1
                        if original - new_dist >= threshold: ans += 1

print(ans)


