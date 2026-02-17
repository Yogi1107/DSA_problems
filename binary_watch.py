class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(0,12):
            for m in range(0,60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    l = f"{h}:{m:02d}"
                    result.append(l)

        return result


# from itertools import combinations

# class Solution:
#     def readBinaryWatch(self, turnedOn: int) -> list[str]:
#         # These are the actual labels on the watch LEDs
#         # We index them 0-3 for hours, and 4-9 for minutes
#         leds = [
#             (8, "h"), (4, "h"), (2, "h"), (1, "h"),      # Hour LEDs
#             (32, "m"), (16, "m"), (8, "m"), (4, "m"), (2, "m"), (1, "m") # Min LEDs
#         ]
        
#         res = []
        
#         # Select exactly 'turnedOn' number of LEDs from the 10 available
#         for selection in combinations(leds, turnedOn):
#             h_sum = 0
#             m_sum = 0
            
#             for value, unit in selection:
#                 if unit == "h":
#                     h_sum += value
#                 else:
#                     m_sum += value
            
#             # Check if the selection makes a valid time
#             if h_sum < 12 and m_sum < 60:
#                 res.append(f"{h_sum}:{m_sum:02d}")
        
#         return res
