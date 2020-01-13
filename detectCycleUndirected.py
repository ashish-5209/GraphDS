from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.v = v

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def cycleUtil(self, u, visited, parent):
        visited[u] = True
        for i in self.graph[u]:
            if visited[i] == False:
                if self.cycleUtil(i, visited, u) == True:
                    return True
            else:
                if parent != i:
                    return True
        return False

    def cycle(self):
        visited = [False]*self.v
        for i in range(self.v):
            if visited[i] == False:
                if self.cycleUtil(i, visited, -1) == True:
                    return True
        return False

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(0, 3)
g.addEdge(3, 4)
if g.cycle() == True:
    print("Cycle consists.")
else:
    print("Cycle does not consists.")

g1 = Graph(3)
g1.addEdge(0,1)
g1.addEdge(1,2)

if g1.cycle():
    print("Cycle consists.")
else:
    print("Cycle does not consists.")
