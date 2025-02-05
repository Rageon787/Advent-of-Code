puzzle = []
with open("input.txt", "r") as f:
    for line in f:
        puzzle.append(line.strip("\n"))         

directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1,), (1, -1), (-1, 1)]         # List of directions 
to_match = "XMAS" 
ans = 0
for i in range(len(puzzle)):
    for j in range(len(puzzle[0])):  
        if (puzzle[i][j] == 'X'):
            for direction in directions:                                                
                ok = True
                for k in range(4): 
                    next_i = i + k * direction[0]
                    next_j = j + k * direction[1]
                    if next_i < 0 or next_i >= len(puzzle) or next_j < 0 or next_j >= len(puzzle[0]) or puzzle[next_i][next_j] != to_match[k]:
                        ok = False
                        break 
                if (ok):
                    ans += 1

print(ans)
                    
