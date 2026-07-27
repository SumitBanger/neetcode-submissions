class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # we need exactly n - 1 edge for it to be a possible Tree
            return False

        parent = [i for i in range(n)]
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Optimisation
                node = parent[node]
            return node
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 == par2:
                return False
            parent[par1] = par2
            return True

        for node1, node2 in edges:
            if not union(node1, node2): return False
        return True

        # adj_list = {i:[] for i in range(n)}
        # for node1, node2 in edges:
        #     adj_list[node1].append(node2)
        #     adj_list[node2].append(node1)

        # visited = set()
        # def dfs(current, prev):
        #     if current in visited:
        #         return False

        #     visited.add(current)
        #     for adjNode in adj_list[current]:
        #         if adjNode == prev:
        #             continue
        #         if not dfs(adjNode, current): return False
        #     return True

        # return dfs(0, -1) and len(visited) == n
        