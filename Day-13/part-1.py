import re


def solve(machine):
    machine = tuple(zip(machine[0], machine[1], machine[2]))
    ans = float("inf")
    x, y = machine[0], machine[1]
    for i in range(101):
        for j in range(101):
            lhs1 = i * int(x[0]) + j * int(x[1]) 
            rhs1 = int(x[2]) 

            lhs2 = i * int(y[0]) + j * int(y[1]) 
            rhs2 = int(y[2])
            if lhs1 == rhs1 and lhs2 == rhs2: ans = min(ans, i * 3 + j) 
    if ans == float("inf"): ans = 0
    return ans 

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
