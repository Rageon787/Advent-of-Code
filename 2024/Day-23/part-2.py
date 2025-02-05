import sys
from collections import defaultdict

filename = sys.argv[1]
edges = []
with open(filename) as f:
    edges = [line.strip().split('-') for line in f] 


adj = defaultdict(set)

for (u, v) in edges:
    adj[u].add(v)
    adj[v].add(u)

visited = set()
vertices_in_component = defaultdict(list)
component, count = 0, 0

def dfs(curr):
    if curr in visited: return
    visited.add(curr) 
    global component
    vertices_in_component[component].append(curr)

    for next in adj[curr]:
        dfs(next)

    return


max_component_size = 0
ans_component = -1

for node in list(adj):
    if node not in visited:
        component += 1
        dfs(node)
        vertex_count = len(vertices_in_component[component]) 
        ok = True
        print(vertices_in_component[component])
        for vertex in vertices_in_component:
            if len(adj[vertex]) != vertex_count - 1: 
                ok = False 
                break
        if ok:
            if vertex_count > max_component_size:
                max_component_size = vertex_count
                ans_component = component


print(f"{ans_component}")

      
A = {}
