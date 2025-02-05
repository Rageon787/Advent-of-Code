nums = []
with open("input.txt") as f:
    input_nums = [str(x) for x in f.read().split()]  

dp = dict()

def convert(x):
    if int(x) == 0: return ["1"] 
    elif len(str(int(x))) % 2 == 0: return [str(int(x[:len(x) // 2])), str(int(x[len(x) // 2:]))] 
    return [str(int(x) * 2024)]
        
def blink(steps, nums):
    ans = 0
    if steps == 25:
        ans += len(nums) 
    else:
        for num in nums:
            if (num, steps) not in dp:
                dp[(num, steps)] = blink(steps + 1, convert(num))
            ans += dp[(num, steps)]            
    
    return ans
    
stones = 0
for num in input_nums:
    stones += blink(0, [num]) 
print(stones) 



