from collections import defaultdict
from queue import Queue

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfsShortestUtil(self, s, d, dist, pred):
        visited = [False]*self.v
        q = Queue()
        q.put(s)
        visited[s] = True
        while q.empty() is False:
            u = q.get()
            for i in self.graph[u]:
                if visited[i] == False:
                    visited[i] = True
                    dist[i] = dist[i] + u
                    pred[i] = u
                    q.put(i)
                    if i == d:
                        return True
        return False

    def bfsShortest(self, s, d):
        dist = [0]*self.v
        pred = [0]*self.v
        pred[s] = -1

        if self.bfsShortestUtil(s, d, dist, pred) is False:
            print("Given Sourse and Destination are not connected.")
            return
        stack = []
        stack.append(d)
        while pred[d] != -1:
            stack.append(pred[d])
            d = pred[d]

        print("Shortest Distance is: ", dist[d])
        print(*stack[::-1])

g = Graph(8)
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(3, 7)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(4, 7)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.bfsShortest(0, 7)
