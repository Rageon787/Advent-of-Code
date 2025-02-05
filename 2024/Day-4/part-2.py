puzzle = []
with open("input.txt", "r") as f:
    for line in f:
        puzzle.append(line.strip("\n"))         

directions = [[(1, 1), (-1, -1,)], [(-1, 1), (1, -1)]]         
ans = 0
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):
        if puzzle[i][j] == 'A': 
            cnt = 0
            for direction in directions:
                if i + direction[0][0] < 0 or i + direction[0][0] >= len(puzzle) or  j + direction[0][1] < 0 or j + direction[0][1] >= len(puzzle[0]):
                    continue
                up = puzzle[i + direction[0][0]][j + direction[0][1]] 
                if i + direction[1][0] < 0 or i + direction[1][0] >= len(puzzle) or  j + direction[1][1] < 0 or j + direction[1][1] >= len(puzzle[0]):
                    continue
                down = puzzle[i + direction[1][0]][j + direction[1][1]]
                if "M" in (up, down) and "S" in (up, down):
                    cnt += 1  
            if cnt == 2:
                ans += 1
print(ans)      
                    
