class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i:[] for i in range(n)}
        for i in range(n): #cria uma lista de adjacencia para cada ponto
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        pq = [(0,0)] # [(cost, point)]
        visited = set()
        total = 0
        while len(visited) < n:
            cost, point = heapq.heappop(pq) #usa uma estrutura de fila prioritaria para visitar sempre o proximo caminho com menor custo
            if point in visited:
                continue
            visited.add(point)
            total += cost
            for cost, point in adj[point]:
                if point not in visited:
                    heapq.heappush(pq, (cost, point))
            
        return total
    
    #Esta implementação tem o desempenho pior pois a heap fica muito grande, realizando muitos pushes
        