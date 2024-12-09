class Node:

    def __init__(self, row, col, direction, Next):
        self.row = row
        self.col = col 
        self.direction = direction
        self.Next = Next


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # North -> east -> south -> west 
grid = [] 
     
with open("sample.txt") as f:
    for line in f:  
        grid.append(list(line.strip("\n")))
n, m = len(grid), len(grid[0]) 

# Initalize a graph with (i, j, direction) 
graph = []
for i in range(n):
    temp1 = []
    for j in range(m):
        temp2 = []
        for d in range(4):
            temp2.append(Node(i, j, d, None))
        temp1.append(temp2)
    graph.append(temp1) 

for i in range(n):
    for j in range(m):
        for (x, y), d in enumerate(directions):
            if i + x >= n or j + y >= m or i + x < 0 or j + y < 0:
                continue
            if grid[i + x][j + y] == "#":
                graph[i][j][d].Next = graph[i][j][(d + 1) % 4] 

# For each (i, j) facing direction (x, y):
    # Your next turning point would be some (p, q) with the next direction     
    # or None, In which case you'll exit the grid 
# Next(i, j, direction) = (p, q, direction) or None

# So, how do you chain these turning points? 
    # First look for the obstruction cells "#", and mark the surrounding cells as the "Turning points" with direction d 
    # Then, your next turning point for (i, j, direction) will be the previous turning point you found with direction * 90deg

    # Iterate top to bottom, to find Next(i, j, North)
        for j in range(m): 
            for i in range(n):               
                if grid[i][j] == "#": continue
                elif i == 0 or j == 0 or i == n - 1 or j == m - 1: continue
                else:
                    if graph[i][j][0].Next == None:
                        graph[i][j][0].Next = graph[i - 1][j][0].Next
                    

        # Iterate right to left, to find Next(i, j, West)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "#": continue
                elif i == 0 or j == 0 or i == n - 1 or j == m - 1: continue
                else:
                    if graph[i][j][3].Next == None:
                        graph[i][j][3].Next = graph[i][j - 1][3].Next 
    
        # Iterate left to right, to find Next(i, j, East)
        for i in range(n):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == "#": continue
                elif i == 0 or j == 0 or i == n - 1 or j == m - 1: continue
                else:
                    if graph[i][j][1].Next == None:
                        graph[i][j][1].Next == graph[i][j][1].Next  

        # Iterate bottom to top, to find Next(i, j, South)
