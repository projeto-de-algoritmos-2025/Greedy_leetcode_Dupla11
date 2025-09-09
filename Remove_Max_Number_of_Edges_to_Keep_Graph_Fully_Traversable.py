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

        # 2) Rotular componentes (0..c-1) no grafo tipo 3
        comp = [-1] * (n + 1)  # comp[0] não usado
        c = self._label_components(g3, n, comp)

        # (temporário) retornar quantas componentes achamos
        return c  # apenas para ver algo funcional por enquanto

    # -------- Helpers --------
    def _label_components(self, g: List[List[int]], n: int, comp: List[int]) -> int:
        """BFS para rotular componentes no grafo g (vértices 1..n). Retorna c."""
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

