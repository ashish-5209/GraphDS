from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        stack.append(v)

    def reverseGraph(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    def printSCCs(self):
        visited = [False]*(self.V)
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        gr = self.reverseGraph()
        visited = [False]*(self.V)
        count = 0
        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                count += 1
                print()
        print(count)

g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)


print ("Following are strongly connected components " +
                           "in given graph")
g.printSCCs()
