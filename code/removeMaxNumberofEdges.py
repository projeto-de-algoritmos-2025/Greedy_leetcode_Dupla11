class UF: #estrutura DSU com um ajuste
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [1] * (n)

    def find(self,x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        n1, n2 = self.find(x1), self.find(x2)
        if n1 == n2:
            return False
        if self.rank[n1] < self.rank[n2]:
            self.par[n1] = n2
            self.rank[n2] += self.rank[n1]
        else:
            self.par[n2] = n1
            self.rank[n1] += self.rank[n2]
        self.n -= 1 #mantem a contagem de quantas arestas foram utilizadas dentro do conjunto
        return True

    def isConnected(self):
        return self.n == 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UF(n), UF(n)
        edge_count = 0

        for tp, src, dest in edges: #verifica primeiro as arestas em que os dois podem atravessar
            if tp == 3:
                ma = alice.union(src-1, dest-1)
                mb = bob.union(src-1, dest-1)
                if ma or mb:
                    edge_count +=1

        for tp, src, dest in edges:
            if tp == 1:
                if alice.union(src-1, dest-1):
                    edge_count +=1
            if tp == 2:
                if bob.union(src-1, dest-1):
                    edge_count +=1

        if alice.isConnected() and bob.isConnected():
            return len(edges) - edge_count #numero de arestas total - numero de arestas utilizadas = numero de arestas a serem removidas
        return -1
        