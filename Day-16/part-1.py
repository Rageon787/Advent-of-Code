import heapq

grid = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # east -> south -> west -> north 

with open("input.txt") as f:
    for line in f: grid.append(line.strip()) 

n, m = len(grid), len(grid[0]) 
min_heap = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S': heapq.heappush(min_heap, (0, (i, j, 0)))

visited = dict() 
ans = float("inf")
while min_heap:
    (score, pos) = heapq.heappop(min_heap)
    (i, j, direction) = pos  
    
    if grid[i][j] == 'E':
        ans = score 
        break

    if grid[i][j] == '#': continue 

    if pos in visited:
        continue 
    visited[pos] = score
    
    # Go to the next cell in the same direction 
    (dx, dy) = directions[direction]
    heapq.heappush(min_heap, (score + 1, (i + dx, j + dy, direction)))
    # Turn 90 degrees clockwise  
    heapq.heappush(min_heap, (score + 1000, (i, j, (direction + 1) % 4)))
    # Turn 90 degrees counterlockwise
    heapq.heappush(min_heap, (score + 1000, (i, j, ((direction - 1) + 4) % 4)))

print(ans)
    


