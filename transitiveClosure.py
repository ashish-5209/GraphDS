from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, s, d):
        self.tc[s][d] = 1
        for i in self.graph[d]:
            if self.tc[s][i] == 0:
                self.DFSUtil(s, i)

    def transitiveClosue(self):
        for i in range(self.V):
            self.DFSUtil(i, i)
        print(self.tc)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.transitiveClosue()
