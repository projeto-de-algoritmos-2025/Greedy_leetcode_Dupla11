class UnionFind: #estrutura do DSU
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.n = n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        self.n -=1
        return True
    def isConnected(self):
      return self.n == 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n= len(points)
        edges = []
        for i in range(n): #gera todas as arestas
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append([dist, i, j])
        
        edges.sort(key=lambda x: x[0]) #ordena as arestas por peso crescente
        uf = UnionFind(n)
        res = 0
        for cost, a, b in edges:
            if uf.union(a, b):
                res += cost
                if uf.isConnected(): #verifica se todo o grafo ja esta conectado (MST gerada)
                    break           
        return res
        