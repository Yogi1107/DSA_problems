# class Solution:
#     def checkRecord(self, s: str) -> bool:
#         from collections import Counter
#         ds = Counter(s)
#         for i in ds.keys():
#             if ds['A'] >= 2 or 'LLL' in s:
#                 return False

#         return True

class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        late_streak = 0

        for ch in s:
            if ch == 'A':
                absences += 1
                if absences >= 2:
                    return False
                late_streak = 0
            elif ch == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:
                late_streak = 0

        return True
