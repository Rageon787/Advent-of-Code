ans = []
def solve(idx, curr, target):
    ok = False
    if idx == len(nums) - 1: 
        if curr == target:
            ok = True
    else:
        ok |= solve(idx + 1, curr * nums[idx + 1], target) 
        ok |= solve(idx + 1, curr + nums[idx + 1], target)
        ok |= solve(idx + 1, int(str(curr) + str(nums[idx + 1])), target)

    return ok


ans = 0
with open("input.txt") as f:
    for line in f:
        res = int(line[:line.index(":")])
        nums = [int(x) for x in line[line.index(":") + 1:].split()]
        if solve(0, nums[0], res): ans += res

print(ans)
        
                
                
                

