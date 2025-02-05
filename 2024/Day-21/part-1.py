import sys 
import re
from itertools import permutations 

filename = sys.argv[1]

numeric_keypad = [["7", "8", "9"],
                  ["4", "5", "6"],
                  ["1", "2", "3"],
                  [" ", "0", "A"]]

numeric_mapping = dict()

for i in range(len(numeric_keypad)):
    for j in range(len(numeric_keypad[0])):
        numeric_mapping[numeric_keypad[i][j]] = (i, j)

directional_keypad = [[" ", "^", "A"],
                      ["<", "v", ">"]]

directional_mapping = dict()

for i in range(len(directional_keypad)):
    for j in range(len(directional_keypad[0])):
        directional_mapping[directional_keypad[i][j]]= (i, j) 

# Permutations of all shortest instructions between 2 cells in a grid

def generate_paths(x, y):
    """returns every permutation of shortest paths from cell X to another cell Y""" 
    (xi, xj) = x
    (yi, yj) = y
    (di, dj) = ((yi - xi), (yj - xj)) 
    instructions = "" 
    if di > 0: instructions += "v" * di
    if di < 0: instructions += "^" * abs(di) 
    if dj > 0: instructions += ">" * dj
    if dj < 0: instructions += "<" * abs(dj)

    return set(["".join(p) for p in permutations(instructions)])

path_permutations = dict()
for xi in range(len(numeric_keypad)):
    for xj in range(len(numeric_keypad[0])):
        for yi in range(len(numeric_keypad)): 
            for yj in range(len(numeric_keypad[0])):
                x = (xi, xj) 
                y = (yi, yj)
                path_permutations[(x, y)] = generate_paths(x, y) 


# The shortest instruction on your directional keypad to make the target robot
shortest_paths = dict()         


visited = set() 

def robot1(path):
    prev = "A"
    paths = [""]
    for curr in path: 
        x = directional_mapping[prev] 
        y = directional_mapping[curr]
        replace_path = []
        for path in paths: 
            for new_path in path_permutations[(x, y)]: 
                replace_path.append(path + new_path + "A")
        paths = replace_path 
        prev = curr
    return paths



def robot2(path):
    prev = "A"
    paths = [""]
    for curr in path: 
        x = directional_mapping[prev] 
        y = directional_mapping[curr]
        replace_path = []
        for path in paths: 
            for new_path in path_permutations[(x, y)]: 
                replace_path.append(path + new_path + "A")
        paths = replace_path 
        prev = curr
    return paths

def you(path):
    prev = "A"
    paths = [""]
    for curr in path: 
        x = directional_mapping[prev] 
        y = directional_mapping[curr]
        replace_path = []
        for path in paths: 
            for new_path in path_permutations[(x, y)]: 
                replace_path.append(path + new_path + "A")
        paths = replace_path 
        prev = curr
    return paths

def precompute():
    n, m = len(numeric_keypad), len(numeric_keypad[0])
    for xi in range(n):
        for xj in range(m): 
            for  yi in range(n):
                for yj in range(m):
                    x = (xi, xj)
                    y = (yi, yj)
                    ans = float("inf") 
                    for p in path_permutations[(x, y)]: 
                        r1 = robot1(p + "A")   
                        for path1 in r1:
                            r2 = robot2(path1 + "A") 
                            for path2 in r2: 
                                y1 = you(path2 + "A")
                                for y_path in y1: 
                                    ans = min(ans, len(y_path))
                    shortest_paths[(numeric_keypad[xi][xj], numeric_keypad[yi][yj])] = ans

precompute()

with open(filename) as f:
    for code in f:
        code = code.strip('\n')
        num_code = int("".join(re.findall(r"\d+", code)))
        prev = "A"
        ans = 0
        for curr in code: 
            ans += shortest_paths[(prev, curr)] 
        print(f"{code} {ans} {num_code}")

