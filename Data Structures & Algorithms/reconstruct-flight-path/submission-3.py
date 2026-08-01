class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        graph, iternary = defaultdict(list), []
        for src, dest in tickets:
            graph[src].append(dest)
        
        def dfs(airport):
            while graph[airport]:
                nextAirport = graph[airport].pop()
                dfs(nextAirport)
            
            iternary.append(airport)
        
        dfs("JFK")
        return iternary[::-1]

        # tickets.sort()
        # adj_list, result = defaultdict(list), ["JFK"]
        # for src, dest in tickets:
        #     adj_list[src].append(dest)

        # def dfs(src):
        #     if len(result) == len(tickets) + 1:
        #         return True
        #     if src not in adj_list:
        #         return False
        #     tempAdjList = adj_list[src]
        #     for index, dest in enumerate(tempAdjList):
        #         adj_list[src].pop(index)
        #         result.append(dest)
        #         if dfs(dest): return True
        #         adj_list[src].insert(index,dest)
        #         result.pop()
        #     return False
                    
        # dfs("JFK")
        # return result
        