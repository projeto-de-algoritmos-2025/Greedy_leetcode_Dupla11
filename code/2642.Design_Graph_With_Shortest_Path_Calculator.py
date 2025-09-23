import heapq
from typing import List


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        """Cria o grafo como uma lista de adjacência """
        self.size = n
        self.graph = [[] for _ in range(n)]
        for e in edges:
            self.graph[e[0]].append([e[1], e[2]])

    def addEdge(self, edge: List[int]) -> None:
        """ Adiciona uma aresta ao grafo """
        self.graph[edge[0]].append([edge[1], edge[2]])
        pass

    def shortestPath(self, node1: int, node2: int) -> int:
        """ Calcula o caminho mais curto entre dois nós usando Dijkstra com fila de prioridade """
        # Inicializa a distância de todos os nós como infinito
        dist = [float('inf') for _ in range(self.size)]

        # Cria uma fila de prioridade e adiciona o nó inicial e define sua distância como 0
        pq = []
        heapq.heappush(pq, [0, node1])
        dist[node1] = 0
        while pq:
            u_weight, u = heapq.heappop(pq)

            # node2 já foi visitado e temos o menor caminho garantido.
            if u == node2:
                # pode retonar sem visitar o resto do grafo.
                return u_weight

            for v in self.graph[u]:
                w, weight = v[0], v[1]

                # Se a nova distância para v for menor que a distancia atual até v
                if dist[w] > dist[u] + weight:
                    dist[w] = int(dist[u] + weight)
                    # Adiciona V na heap
                    heapq.heappush(pq, [dist[w], w])

        # Se não existe caminho de node1 até node2
        if dist[node2] == float('inf'):
            return -1
        return dist[node2]
