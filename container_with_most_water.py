class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            max_water = max(max_water, width * current_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

class Solution:
    def maxArea(self, height):
        max_area = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                current_height = min(height[i], height[j])
                area = width * current_height
                max_area = max(max_area, area)

        return max_area

