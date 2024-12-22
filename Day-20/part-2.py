import sys 
import heapq
from collections import deque
filename = sys.argv[1]

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
start, end = (0, 0), (0, 0)
visited = dict()
visited2 = set()
ans = 0
def djikstra(src): 
    global ans
    min_heap = [(0, src)] 
    while min_heap:  
        dist, (x, y) = heapq.heappop(min_heap) 

        if (src, x, y) in visited or grid[x][y] == '#': continue 
        visited[(src, x, y)] = dist



        if src == start:
            queue = deque([]) 
            queue.append((0, (x, y)))
            start_cheat = (x, y)
            while queue: 
                cheat_time, (cx, cy) = queue.popleft() 
                end_cheat = (cx, cy)
                if (start_cheat, end_cheat) in visited2: continue 
                visited2.add((start_cheat, end_cheat))
                if (end, cx, cy) in visited: 
                    new_dist = visited[(end, cx, cy)] + dist + cheat_time 
                    if original - new_dist >= threshold:
                        ans += 1

                if cheat_time == 20: continue           

                for (dx, dy) in directions: 
                    if cx + dx in range(n) and cy + dy in range(m):
                        queue.append((cheat_time + 1, (cx + dx, cy + dy)))


        for (dx, dy) in directions: 
            if x + dx not in range(n) or y + dy not in range(m): continue
            heapq.heappush(min_heap, (dist + 1, (x + dx, y + dy))) 

grid = []
with open(filename) as f:
    for line in f:
        grid.append(list(line.strip())) 

n, m = len(grid), len(grid[0])
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j) 
        if grid[i][j] == 'E': 
            end = (i , j) 

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'E':
            djikstra((i, j))


original, threshold = visited[(end, start[0], start[1])], 100
ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S': 
            djikstra((i, j)) 

print(ans)
