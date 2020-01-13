from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, u, visited):
        visited[u] = True
        for i in self.graph[u]:
            if visited[i] is False:
                self.DFS(i, visited)

    def motherVertex(self):
        visited = [False]*(self.V)

        res = 0

        for i in range(self.V):
            if visited[i] is False:
                self.DFS(i, visited)
                res = i

        visited = [False]*self.V
        self.DFS(res, visited)

        for i in visited:
            if i is False:
                return -1
        return res

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)

print(g.motherVertex())
