# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         mapST = {}
#         mapTS = {}

#         for c1, c2 in zip(s, t):
#             if c1 in mapST and mapST[c1] != c2:
#                 return False
#             if c2 in mapTS and mapTS[c2] != c1:
#                 return False

#             mapST[c1] = c2
#             mapTS[c2] = c1

#         return True


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        t_used = set()

        for ch_s, ch_t in zip(s,t):

            if ch_s not in map_s:

                if ch_t in t_used:
                    return False
                map_s[ch_s] = ch_t
                t_used.add(ch_t)

            else:
                if map_s[ch_s] != ch_t:
                    return False

        
        return True
            
