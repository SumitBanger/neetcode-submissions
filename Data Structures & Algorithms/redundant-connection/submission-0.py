class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(0, len(edges) + 1)]
        print(parent)
        def find(node):
            print(node)
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return False
            parent[par1] = par2
            return True

        for node1, node2 in edges:
            if not union(node1, node2): return [node1, node2]
        return []
