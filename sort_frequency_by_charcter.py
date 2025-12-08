class Solution:
    def frequencySort(self, s: str) -> str:
        result = {}
        lst = list(s)
        
        for i in lst:
            result[i] = result.get(i, 0) + 1
        
        result_s = ""
        
        for i in sorted(result.keys(), key=lambda x: result[x], reverse=True):
            result_s += i * result[i]  
        
        return result_s


# class Solution:
#     def frequencySort(self, s: str) -> str:
#         d=Counter(s)
#         f=""
#         if len(s)==1:
#             return a
#         while d:

#             m=max(d.values())
#             l=[x for x in d.keys() if d[x]==m]
#             for x in l:
#                 f+=x*d[x]
#                 del d[x]
        
#         return f
