from collections import  defaultdict
from queue import Queue

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False]*(len(self.graph))
        q = Queue()
        visited[s] = True
        q.put(s)

        while q.empty() is False:
            v = q.get()
            print(v, end=" ")

            for i in self.graph[v]:
                if visited[i] is False:
                    q.put(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)
