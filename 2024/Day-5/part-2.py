rules = []
updates = []
ok = False


with open("input.txt", "r") as f: 
    for line in f:
        line = line.strip("\n")
        if line == "":
            ok = True  
            continue
        if not ok: rules.append([int(x) for x in line.split("|")]) 
        else: updates.append([int(x) for x in line.split(",")])


adj = dict() 

for rule in rules:
    a, b = rule[0], rule[1]
    if a not in adj:
        adj[a] = set()
    if b not in adj:
        adj[b] = set()
    adj[a].add(b)

incorrect_updates = []
for update in updates:
    ok = True
    visited = set() 
    for x in update:
        for y in adj[x]:
            if y in visited: 
                ok = False
                break
        if not ok: break
        visited.add(x)
    if not ok:
        incorrect_updates.append(update)
ans = 0
for update in incorrect_updates:
    for i in range(len(update)):
        while True:
            changed = False 
            for j in range(i):
                if update[j] in adj[update[i]]:
                    update[i], update[j] = update[j], update[i] 
                    changed = True             
                    break
            if not changed: break
    ans += update[len(update) // 2]        

print(ans) 



