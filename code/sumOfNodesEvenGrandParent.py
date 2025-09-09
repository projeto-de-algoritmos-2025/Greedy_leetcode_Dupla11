class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, parent = None, grandparent = None):
            if not node: #verifica se o nó existe
                return 0
            
            total = 0
            # faz a busca com dfs, somando ao total sempre que encontrar um avô par
            if grandparent and grandparent.val % 2 == 0:
                total += node.val
            total += dfs(node.left, node, parent)
            total += dfs(node.right, node, parent)
            return total
          
        return dfs(root)
