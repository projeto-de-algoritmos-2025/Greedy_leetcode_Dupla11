import heapq
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):

        self.size = n
        self.graph = [[] for _ in range(n)]
        for e in edges:
            self.graph[e[0]].append([e[1], e[2]])
        pass

    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])
        pass

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [float('inf') for _ in range(self.size)]
        pq = []
        heapq.heappush(pq, node1)
        dist[node1] = 0

        while pq:
            u = heapq.heappop(pq)
            for v in self.graph[u]:
                heapq.heappush(pq,v)
        pass


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
