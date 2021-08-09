from collections import defaultdict
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v)
def gen_edges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node,neighbor))
    print(edges)
ch = input("\nDo you want to enter first edge (y/n) ? : ")
while ch == 'y':
    if ch == 'y':
        ch = input("\nDo you want to continue adding edges (y/n) ? : ")
        if ch == 'y':
            node1 = input("\n Enter Node 1 : ")
            node2 = input("\n Enter Node 2 : ")
            addEdge(graph,node1,node2)
        elif ch == 'n':
            continue
gen_edges(graph)
