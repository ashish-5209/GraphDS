from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, connected, count):

        print(v, end=" ")
        visited[v] = True
        connected[v] = count

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, connected, count)


    def DFS(self):
        n = len(self.graph)
        visited = [False]*n
        connected = [-1]*n
        count = 0

        for i in range(n):
            if visited[i] is False:
                self.DFSUtil(i, visited, connected, count)
                count += 1
        print()
        print(*connected)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(4, 5)
g.addEdge(5, 4)
g.addEdge(6, 6)

print("Following is Depth First Traversal")
g.DFS()
