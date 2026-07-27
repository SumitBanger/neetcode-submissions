class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj_list = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()
        def dfs(current, prev):
            if current in visited:
                return False

            visited.add(current)
            for adjNode in adj_list[current]:
                if adjNode == prev:
                    continue
                if not dfs(adjNode, current): return False
            return True

        return dfs(0, -1) and len(visited) == n
        