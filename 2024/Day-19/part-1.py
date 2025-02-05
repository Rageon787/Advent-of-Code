import sys 
 
filename = sys.argv[1]
with open(filename) as f: 
    raw_input = f.read().split('\n')
    patterns = raw_input[0].strip().split(', ')
    designs = [design.strip('\n') for design in raw_input[2:-1]]

ans = 0
for design in designs:
    n = len(design) 
    dp = [0] * (n + 1)
    for i in range(n): 
        for pattern in patterns: 
            left = i - len(pattern) 
            if left < -1: continue
            sub_design = design[left + 1:i + 1]
            if sub_design == pattern:
                if left == -1: dp[i] += 1
                else: dp[i] += dp[left]
    if dp[n - 1] > 0: ans += 1
print(ans)
