from collections import defaultdict
from queue import Queue
class Graph:

    def __init__(self):
        self.city = defaultdict(list)

    def addCity(self, src, dest):
        self.city[src].append(dest)
        self.city[dest].append(src)

    def printList(self):
        for k in self.city:
            print(k, end=": ")
            for i in self.city[k]:
                print(i, end="-->")
            print()

    def bfs(self, v):
        q = Queue()
        q.put(v)

        visited = {}
        for i in self.city:
            visited[i] = False
        visited[v] = True


        while q.empty() is False:
            temp = q.get()
            print(temp, end=" ")

            for i in self.city[temp]:
                if visited[i] is False:
                    q.put(i)
                    visited[i] = True

g = Graph()
g.addCity("Amritsar", "Delhi")
g.addCity("Amritsar", "Jaipur")
g.addCity("Delhi", "Ranchi")
g.addCity("Delhi", "Bangalore")
g.addCity("Delhi", "Agra")
g.addCity("Amritsar", "Ranchi")

g.printList()
g.bfs("Amritsar")
