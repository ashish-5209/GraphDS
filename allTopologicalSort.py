from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def top_order_Util(self, visited, lis, stack):
        flag = False

        for i in range(self.V):
            if not visited[i] and lis[i] == 0:
                visited[i] = True
                stack.append(i)

                for j in self.graph[i]:
                    lis[j] -= 1

                self.top_order_Util(visited, lis, stack)
                visited[i] = False
                stack.pop()
                for j in range(i):
                    lis[j] += 1

                flag = True

        if not flag:
            print(*stack)

    def top_order(self):
        visited = [False]*self.V
        lis = [0]*self.V

        for i in range(self.V):
            for j in self.graph[i]:
                lis[j] += 1

        stack = []

        self.top_order_Util(visited, lis, stack)

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

g.top_order()
