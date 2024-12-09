from collections import defaultdict


with open("input.txt") as f: 
    grid = [list(line.strip("\n")) for line in f]     
n, m = len(grid), len(grid[0])


antennas = defaultdict(list)
for i in range(n):
    for j in range(m):
        if grid[i][j] != '.':
            antennas[grid[i][j]].append((i, j))
ans = set()
for frequency in antennas:
    for i in range(len(antennas[frequency])):
        (x1, y1) = antennas[frequency][i]
        ans.add((x1, y1))
        for j in range(i + 1, len(antennas[frequency])):
            (x2, y2) = antennas[frequency][j]
            ans.add((x2, y2))
            dx = x1 - x2
            dy = y1 - y2
        
            antinode1 = (x1 + dx, y1 + dy) 
            while antinode1[0] < n and antinode1[0] >= 0 and antinode1[1] < m and antinode1[1] >= 0:
                ans.add(antinode1)
                grid[antinode1[0]][antinode1[1]] = "#"
                antinode1 = (antinode1[0] + dx, antinode1[1] + dy) 
            
            antinode2 = (x2 - dx, y2 - dy)
            while antinode2[0] >= 0 and antinode2[0] < n and antinode2[1] >= 0 and antinode2[1] < m:
                ans.add(antinode2)
                grid[antinode2[0]][antinode2[1]] = "#"
                antinode2 = (antinode2[0] - dx, antinode2[1] - dy)

for g in grid: print(g) 
print(len(ans))
            