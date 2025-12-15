# class Solution:
#     def validateCoupons(
#         self,
#         code: List[str],
#         businessLine: List[str],
#         isActive: List[bool]
#     ) -> List[str]:

#         valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
#         order = {line: i for i, line in enumerate(valid_lines)}
#         result = []

#         for c, b, active in zip(code, businessLine, isActive):
#             if not c:
#                 continue
#             if not all(ch.isalnum() or ch == "_" for ch in c):
#                 continue
#             if b not in order:
#                 continue
#             if not active:
#                 continue

#             result.append((order[b], c))

#         result.sort()
#         return [c for _, c in result]


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        k=[]
        b=set(["electronics", "grocery", "pharmacy", "restaurant"])
        for i in range(len(code)):
            if isActive[i] != True or businessLine[i] not in b or code[i] == '':
                continue
            l=code[i].split('_')
            f=1
            for j in l:
                if j and j.isalnum() == False:
                    f=0
                    break
            if f:
                k.append([businessLine[i], code[i]])
        k.sort()
        ans=[i for _,i in k]
        return ans
