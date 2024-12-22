import sys 
from collections import deque, defaultdict
filename = sys.argv[1]
mod = 16777216




def next_secret(secret_num):
    result = secret_num * 64 # multiply by 64
    secret_num ^= result
    secret_num %= mod 

    result = secret_num // 32 
    secret_num ^= result
    secret_num %= mod
    
    result = secret_num * 2048 
    secret_num ^= result
    secret_num %= mod

    return secret_num

with open(filename) as f:
    nums = f.read().split('\n') 


sequences = defaultdict(list)
for num in nums:
    if num == '': continue
    secret_num = int(num)  
    secret_nums = [secret_num % 10] 
    changes = []
    for j in range(2000): 
        secret_num = next_secret(secret_num)
        changes.append((secret_num % 10) - secret_nums[-1])
        secret_nums.append(secret_num % 10) 
    visited = set() 
    sequences[tuple(changes[0:4])].append(secret_nums[4])
    visited.add(tuple(changes[0:4]))
    last_changes = deque(changes[0:4]) 

    for i in range(len(changes)): 
        last_changes.popleft() 
        last_changes.append(changes[i]) 
        curr_sequence = tuple(last_changes)
        if curr_sequence not in visited: 
            sequences[curr_sequence].append(secret_nums[i + 1])
            visited.add(curr_sequence)

ans = 0
for sequence in sequences: 
    ans = max(ans, sum(sequences[sequence]))
print(ans)

