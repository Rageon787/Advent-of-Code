import sys 

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

ans = 0

for num in nums:
    if num == '': continue
    secret_num = int(num)  
    for j in range(2000): 
        secret_num = next_secret(secret_num) 
    ans += secret_num
print(ans)
