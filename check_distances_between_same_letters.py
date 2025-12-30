class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first_pos = {}

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')

            if ch not in first_pos:
                first_pos[ch] = i
            else:
                if i - first_pos[ch] - 1 != distance[idx]:
                    return False

        return True
