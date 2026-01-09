class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        from collections import Counter
        dict_ = Counter(nums)
        length = len(nums)
        set_nums = set(nums)
        for i in dict_.keys():
            if length == 2 * dict_[i] and len(set_nums) == dict_[i] + 1 and dict_[i] == length // 2:
                return i

# class Solution:
#     def repeatedNTimes(self, a: List[int]) -> int:
#         d={}
#         for i in a:
#             if i in d:
#                 return i
#             d[i]=1

        
