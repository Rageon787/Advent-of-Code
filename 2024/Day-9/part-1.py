from collections import deque, defaultdict

with open("input.txt") as f:
    disk_map = f.read().strip()    

result = []
file_id = 0
for i in range(len(disk_map)):
    
    if i % 2 == 0:
        for j in range(int(disk_map[i])):
            result.append(file_id) 
        file_id += 1
    else: 
        for j in range(int(disk_map[i])):
            result.append(-1)


l, r = 0, len(result) - 1


while l <= r:
    if result[l] == -1:
        while result[r] == -1: r -= 1
        if r < l: break
        result[l], result[r] = result[r], result[l]
        l += 1 
        r -=1
    else: l += 1
ans = 0
for i in range(len(result)):
    if result[i] == -1: break
    ans += result[i] * i

print(ans)
