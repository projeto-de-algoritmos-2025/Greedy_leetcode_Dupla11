# solution.py
from collections import deque
from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 1) Grafo apenas com arestas do tipo 3
        g3 = [[] for _ in range(n + 1)]
        for t, u, v in edges:
            if t == 3:
                g3[u].append(v)
                g3[v].append(u)

        # 2) Componentes no grafo tipo 3
        comp = [-1] * (n + 1)
        c = self._label_components(g3, n, comp)

        # 3) Construir grafos por componentes para Alice (tipo1) e Bob (tipo2)
        h1 = [[] for _ in range(c)]
        h2 = [[] for _ in range(c)]
        for t, u, v in edges:
            cu, cv = comp[u], comp[v]
            if cu == cv:
                continue  # aresta dentro da mesma componente compartilhada não conecta componentes
            if t == 1:
                h1[cu].append(cv); h1[cv].append(cu)
            elif t == 2:
                h2[cu].append(cv); h2[cv].append(cu)
            # t == 3 nunca ligará componentes diferentes, pois comp foi gerado com o próprio tipo 3

        # (temporário) devolvera o número de nós de H1/H2 para debugar
        return (len(h1), len(h2))  # só para inspecionar

    # -------- Helpers --------
    def _label_components(self, g: List[List[int]], n: int, comp: List[int]) -> int:
        c = 0
        for start in range(1, n + 1):
            if comp[start] != -1:
                continue
            comp[start] = c
            q = deque([start])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if comp[v] == -1:
                        comp[v] = c
                        q.append(v)
            c += 1
        return c
