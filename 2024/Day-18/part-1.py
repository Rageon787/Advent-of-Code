from collections import deque
import sys

filename = sys.argv[1] 

corrupted_bytes = []
with open(filename) as f:
    for line in f:
        line = line.strip() 
        nums = (int(x) for x in line.split(','))
        corrupted_bytes.append(nums)

k = 1024
n, m = 71, 71

grid = [["."] * m for _ in range(n)]

for i, (x, y) in enumerate(corrupted_bytes):
    if i == k: break
    print((x, y))
    grid[y][x] = '#'

start_pos = (0, 0)
queue = deque()
queue.append((0, start_pos))

visited = set() 
ans = -1
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
while queue:
    dist, (x, y) = queue.popleft() 
    if x not in range(n) or y not in range(m) or (x, y) in visited or grid[x][y] == '#': 
        continue
    visited.add((x, y))
    if x == n - 1 and y == m - 1: 
        ans = dist 
        break
    for (dx, dy) in directions:
        queue.append((dist + 1, (x + dx, y + dy)))

print(ans)

    

