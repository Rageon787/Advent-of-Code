from collections import deque, defaultdict

def fill_blocks(empty_range, file_range, not_moved):
    [ex, ey] = empty_range     
    empty_size = ey - ex + 1
    if ex <= ey:
        for file_id in not_moved:
            [fx, fy] = file_range[file_id] 
            if fy < ex: continue
            block_size = fy - fx + 1             
            if block_size <= empty_size:
                empty_range = [ex + block_size, ey]
                file_range[file_id] = [ex, ex + block_size - 1]
                not_moved.remove(file_id) 
                fill_blocks(empty_range,file_range, not_moved)
                break
    return 

                

with open("input.txt") as f:
    disk_map = f.read().strip()    

file_id, curr_idx = 0, 0
file_range = defaultdict(list) 
file_block = defaultdict(list)
empty_blocks = []

for i in range(len(disk_map)):
    [x, y] = [curr_idx, curr_idx + int(disk_map[i]) - 1] 
    block_size = y - x + 1
    
    if i % 2 == 0:
        file_range[file_id] = [x, y]
        file_block[block_size].append(file_id) 
        file_id += 1
    else:
        empty_blocks.append([x, y]) 

    curr_idx += block_size

for file_id in file_range:
    [x, y] = file_range[file_id]
not_moved = [i for i in range(len(file_range) - 1, -1, -1)] 

for empty_block in empty_blocks:
    fill_blocks(empty_block, file_range, not_moved)


ans = 0 
for file_id in file_range:
    [x, y] = file_range[file_id]
    ans += file_id * sum(range(x, y + 1)) 
print(ans)

             
    

