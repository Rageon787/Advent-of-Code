import re 


n, m = 103, 101                      # Change this 103, 101 for actual input
robots = []
with open("input.txt") as f:
    for line in f:
        nums = re.findall(r"-?\d+", line)  
        nums = [int(x) for x in nums]
        p, v = (nums[1], nums[0]), (nums[3], nums[2])
        robots.append([p, v]) 
print(len(robots))
old_grid = [[0] * m for _ in range(n)]  
for robot in robots:  
    old_grid[robot[0][0]][robot[0][1]] += 1


curr_time = 0
while curr_time < 100:
    for robot in robots:
        (x, y), (dx, dy) = robot  
        robot[0] = [((x + dx) + n) % n, ((y + dy) + m) % m]
    curr_time += 1
    visited = set()
    count_component = 0
    for robot in robots:
        if robot not in visited:  
            count_component += 1
            dfs(robot[0], visited, )
    if count_component == 1:
        print(curr_time)
        break

        

    
new_grid = [[0] * m for _ in range(n)]  
for robot in robots:  
    new_grid[robot[0][0]][robot[0][1]] += 1

quadrant = [[0] * 2 for _ in range(2)]  
x, y = 0, 0
for i in range(n): 
    if i == n // 2: 
        x += 1 
        continue 
    for j in range(m):  
        if j == m // 2: 
            y += 1
            continue 
        quadrant[x][y] += new_grid[i][j]
    y = 0 

ans = 1
for i in range(2):
    for j in range(2): ans *= quadrant[i][j]

print(ans)
