class Graph:
    def __init__(self):
        self.graph = defaultdic(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

graph = Graph()
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)
print(graph.graph)