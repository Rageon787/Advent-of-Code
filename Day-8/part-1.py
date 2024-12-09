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
        for j in range(i + 1, len(antennas[frequency])):
            (x2, y2) = antennas[frequency][j]
            dx = x1 - x2
            dy = y1 - y2
        
            antinode1 = (x1 + dx, y1 + dy) 
            if antinode1[0] < n and antinode1[0] >= 0 and antinode1[1] < m and antinode1[1] >= 0: ans.add(antinode1)                        
            antinode2 = (x2 - dx, y2 - dy)
            if antinode2[0] < n and antinode2[0] >= 0 and antinode2[1] < m and antinode2[1] >= 0: ans.add(antinode2)


for g in grid: print(g) 
print(len(ans))
            