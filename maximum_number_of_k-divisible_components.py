# class Solution:
#     def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
#         from collections import defaultdict
        
#         graph = defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)
        
#         res = 0
        
#         def dfs(node, parent):
#             nonlocal res
#             total = values[node]
            
#             for child in graph[node]:
#                 if child != parent:
#                     total += dfs(child, node)
            
#             if total % k == 0:
#                 res += 1
#                 return 0  # reset because this becomes a separate component
            
#             return total
        
#         dfs(0, -1)
#         return res


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        def dfs(node, parent):
            cursum = values[node]
            for nei in adj_list[node]:
                if nei == parent: continue
                cursum += dfs(nei, node)
            if cursum%k==0:
                self.ans += 1
                return 0
            return cursum

        adj_list = [[] for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        self.ans = 0
        dfs(0, -1)
        return self.ans
