class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]
        result = n

        def find(node): # Responsible for finding the topmost parent of given node
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(node1, node2): # Responsible for merging both nodes based on Rank
            par1, par2 = find(node1), find(node2)

            if par1 == par2: # Both the nodes already have common parent so are already connected so no need of union
                return 0

            if rank[par1] > rank[par2]:
                parent[par2] = par1
                rank[par1] += rank[par2]
            else:
                parent[par1] = par2
                rank[par2] += rank[par1]
            return 1

        for node1, node2 in edges:
            result -= union(node1, node2)

        return result
        