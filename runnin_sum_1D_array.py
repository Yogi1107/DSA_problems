# Problem 1480 : Running a Sum of 1d Array

list_ = []
for i in range(1,len(nums)+1):
    list_.append(sum(nums[:i]))
return list_
    
#for i in range(1,len(nums)):
#    nums[i] = nums[i] + nums[i-1]
#return nums