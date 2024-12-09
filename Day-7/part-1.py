ans = 0
with open("input.txt") as f:
    for line in f:
        res = int(line[:line.index(":")])
        nums = [int(x) for x in line[line.index(":") + 1:].split()]
        n = len(nums)
        for i in range(1 << (n - 1)):
            res2 = nums[0]
            for j in range(n - 1):        
                if i & (1 << j) != 0:
                    res2 += nums[j + 1]
                else:
                    res2 *= nums[j + 1]
            
            if res == res2:
                ans += res
                break
                    

print(ans)
        
                
                
                

