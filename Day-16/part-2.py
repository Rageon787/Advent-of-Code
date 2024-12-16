import heapq
from collections import defaultdict, deque
grid = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # east -> south -> west -> north 

with open("input.txt") as f:
    for line in f: grid.append(list(line.strip())) 

n, m = len(grid), len(grid[0]) 
min_heap = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S': heapq.heappush(min_heap, (0, (i, j, 0), (-1, -1, -1)))

visited = dict() 
previous = defaultdict(list) 
ans = float("inf")
while min_heap:
    curr = heapq.heappop(min_heap)
    score = curr[0]
    pos = curr[1]  
    prev_pos = curr[2] 
    (i, j, direction) = pos 
    if grid[i][j] == '#': continue 
    
    if pos in visited:
        if score == visited[pos]: 
            previous[pos].append(prev_pos) 
        else: continue
    else:
        visited[pos] = score
        previous[pos].append(prev_pos)

    if grid[i][j] == 'E':
        if score > visited[pos]: break 
        else: ans = min(ans, score)
        continue 
    # Go to the next cell in the same direction 
    (dx, dy) = directions[direction]
    heapq.heappush(min_heap, (score + 1, (i + dx, j + dy, direction), pos))
    # Turn 90 degrees clockwise  
    heapq.heappush(min_heap, (score + 1000, (i, j, (direction + 1) % 4), pos))
    # Turn 90 degrees counterlockwise
    heapq.heappush(min_heap, (score + 1000, (i, j, ((direction - 1) + 4) % 4), pos))
print(ans)
ans2 = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'E':
            queue = deque()
            for d in range(4): 
                if (i, j, d) in visited and ans == visited[(i, j, d)]:
                    queue.append((i, j, d)) 
            while queue:
                next_previous = queue.popleft()
                if next_previous == (-1, -1, -1): break
                if (next_previous) in ans2: continue         
                ans2.add((next_previous[0], next_previous[1]))
                grid[next_previous[0]][next_previous[1]] = 'O' 
                next_next_previous = set(previous[next_previous])
                for nnp in next_next_previous:
                    queue.append(nnp) 
print(len(ans2))
