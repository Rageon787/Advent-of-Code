import sys
from collections import defaultdict

filename = sys.argv[1]
edges = []
with open(filename) as f:
    edges = [line.strip().split("-") for line in f]

adj = defaultdict(set)

for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)

triplets = set()
ans = set()
for node1 in adj:
    for node2 in adj:
        for node3 in adj:
            if node1 in adj[node2] and node1 in adj[node3] and node2 in adj[node3]:
                triplet = [node1, node2, node3]
                triplet.sort()

                if node1[0] == "t" or node2[0] == "t" or node3[0] == "t":
                    ans.add(tuple(triplet))

print(len(ans))
