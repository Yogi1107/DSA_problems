class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        pattern_lst = []
        for i in pattern:
            pattern_lst.append(i)
        if len(pattern) != len(lst):
            return False
        
        mapST = {}
        mapTS = {}

        for c1, c2 in zip(lst, pattern_lst):
            if c1 in mapST and mapST[c1] != c2:
                return False
            if c2 in mapTS and mapTS[c2] != c1:
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
        
