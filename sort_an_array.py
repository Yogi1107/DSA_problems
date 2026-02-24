# from typing import List

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def merge(nums, left, right, mid):
#             n1 = mid - left + 1
#             n2 = right - mid

#             L = [nums[left + i] for i in range(n1)]
#             R = [nums[mid + 1 + j] for j in range(n2)]

#             i = j = 0
#             k = left

#             while i < n1 and j < n2:
#                 if L[i] <= R[j]:
#                     nums[k] = L[i]
#                     i += 1
#                 else:
#                     nums[k] = R[j]
#                     j += 1
#                 k += 1

#             while i < n1:
#                 nums[k] = L[i]
#                 i += 1
#                 k += 1

#             while j < n2:
#                 nums[k] = R[j]
#                 j += 1
#                 k += 1

#         def mergeSort(nums, left, right):
#             if left < right:
#                 mid = (left + right) // 2
#                 mergeSort(nums, left, mid)
#                 mergeSort(nums, mid + 1, right)
#                 merge(nums, left, right, mid)

#         mergeSort(nums, 0, len(nums) - 1)
#         return nums

class Solution:
    def sortArray(self, nums):
        def heapify(arr, n, i):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(nums)

        
        for i in range(n//2 - 1, -1, -1):
            heapify(nums, n, i)

       
        for size in range(n-1, 0, -1):
            nums[0], nums[size] = nums[size], nums[0]
            heapify(nums, size, 0)

        return nums
