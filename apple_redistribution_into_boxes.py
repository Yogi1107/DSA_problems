class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        current_capacity = 0
        boxes_used = 0
        
        for cap in capacity:
            current_capacity += cap
            boxes_used += 1
            if current_capacity >= total_apples:
                return boxes_used
        
        return boxes_used
