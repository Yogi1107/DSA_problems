class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0

        while i < len(word1) and i < len(word2):
            result += word1[i]
            result += word2[i]
            i += 1

        result += word1[i:]
        result += word2[i:]

        return result


# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         i,j = 0,0
#         ans = []
#         while(i<len(word1) and j<len(word2)):
#             ans.append(word1[i])
#             ans.append(word2[j])
#             i+=1
#             j+=1

#         while(i<len(word1)):
#             ans.append(word1[i])
#             i+=1

#         while(j<len(word2)):
#             ans.append(word2[j])
#             j+=1

#         res = "".join(ans)
#         return res
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
