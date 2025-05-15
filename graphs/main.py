# vertices and edges
# V = vertices
# E = the edges between the vertices
# can be directed or undirected
# can be weighted where the edges have a value

# built using adjacency matrix
# good for many edges
# V^2 space
# checking for edge takes contstant time
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0]* self.V for _ in range(self.V)]

    def add_edge(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

# build using adjacency list
# good for sparse graphs
# V+E space
# accessing neighbors of a vertex is faster
class Graph2:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)