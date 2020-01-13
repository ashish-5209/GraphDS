from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.v = v

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def cycleUtil(self, u, visited, prev):
        visited[u] = True
        prev[u] = True

        for i in self.graph[u]:
            if visited[i] == False and self.cycleUtil(i, visited, prev):
                return True
            elif prev[i] == True:
                return True
        prev[u] = False
        return False

    def cycle(self):
        visited = [False]*self.v
        prev = [False]*self.v

        for i in range(self.v):
            if visited[i] == False:
                if self.cycleUtil(i, visited, prev):
                    return True

        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.cycle():
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
