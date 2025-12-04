class Solution:
    def countCollisions(self, directions: str) -> int:
        # Trim leading L's and trailing R's (they never collide)
        s = directions.lstrip('L').rstrip('R')
        
        # In the remaining string:
        # Every 'L' or 'R' contributes 1 collision
        # 'S' contributes 0
        return len(s) - s.count('S')
