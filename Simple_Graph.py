from collections import defaultdict
graph = defaultdict(list)
def addEdge(graph,u,v):
  graph[u],append(v)
def gen_edges(graph):
  edges = []
  for node in graph:
    for neighbor in graph[node]:
      edges.append((node,neighbor))
addEdge(graph,1,2)
addEdge(graph,1,3)
addEdge(graph,2,3)
print(gen_edges(graph))
