import re
import math

offset = 10000000000000
def solve(machine):
    machine = tuple(zip(machine[0], machine[1], machine[2]))
    ans = float("inf")
    e1, e2 = machine[0], machine[1]
    (a, b, z1) = [int(x) for x in e1] 
    (c, d, z2) = [int(x) for x in e2]
    z1 += offset 
    z2 += offset
    y = ((z2 * a) - (z1 * c)) / ((a * d) - (b * c)) 
    x1 = (z1 - (b * y)) / a 
    x2 = (z2 - (d * y)) / c 
    if x1 != x2: ans = 0  
    elif math.floor(x1) != x1 or math.floor(y) != y: ans = 0
    else: ans = 3 * x1 + y
    return int(ans) 
with open("input.txt") as f:
    res = 0
    temp = []
    for line in f:
        if line == "": continue  
        matches = re.findall(r"\d+", line)
        if matches == []: continue
        temp.append(matches)  
        if len(temp) == 3:
            res += solve(temp) 
            temp = []
    print(res)

