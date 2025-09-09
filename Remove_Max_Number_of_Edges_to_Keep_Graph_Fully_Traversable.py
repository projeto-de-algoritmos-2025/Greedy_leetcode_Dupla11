from collections import deque
from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """
        BFS-only approach.
        1) Usa apenas arestas tipo 3 para rotular componentes compartilhadas (c).
        2) Constrói grafos de componentes H1 (tipo1) e H2 (tipo2).
        3) Verifica conectividade de H1 e H2.
        4) Se ambos conectam, arestas mínimas necessárias = (n - c) + (c - 1) + (c - 1) = n + c - 2.
           Removíveis = len(edges) - (n + c - 2).

        Complexidade: O(n + |edges|).
        """
        # 1) Grafo tipo 3
        g3 = [[] for _ in range(n + 1)]
        for t, u, v in edges:
            if t == 3:
                g3[u].append(v)
                g3[v].append(u)

        # 2) Componentes no grafo tipo 3
        comp = [-1] * (n + 1)
        c = self._label_components(g3, n, comp)

        # 3) Grafos de componentes (Alice/Bob)
        h1 = [[] for _ in range(c)]
        h2 = [[] for _ in range(c)]
        for t, u, v in edges:
            cu, cv = comp[u], comp[v]
            if cu == cv:
                continue
            if t == 1:
                h1[cu].append(cv); h1[cv].append(cu)
            elif t == 2:
                h2[cu].append(cv); h2[cv].append(cu)

        # 4) Conectividade necessária
        if not self._is_connected(h1, c):
            return -1
        if not self._is_connected(h2, c):
            return -1

        # 5) Máximo de arestas removíveis
        needed = n + c - 2
        return len(edges) - needed

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

    def _is_connected(self, h: List[List[int]], c: int) -> bool:
        if c <= 1:
            return True
        seen = [False] * c
        q = deque([0])
        seen[0] = True
        while q:
            u = q.popleft()
            for v in h[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
        return all(seen)

if __name__ == "__main__":
    s = Solution()
    print(s.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))  # 2
    print(s.maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))                  # 0
    print(s.maxNumEdgesToRemove(4, [[3,2,3],[1,1,2],[2,3,4]]))                          # -1
