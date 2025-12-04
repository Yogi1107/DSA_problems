class Solution:
    def countCollisions(self, directions: str) -> int:
        # Trim leading L's and trailing R's (they never collide)
        s = directions.lstrip('L').rstrip('R')
        
        # In the remaining string:
        # Every 'L' or 'R' contributes 1 collision
        # 'S' contributes 0
        return len(s) - s.count('S')



# class Solution {
#     public int countCollisions(String directions) {
#         int left = 0;
#         while (left < directions.length() && directions.charAt(left) == 'L') {
#             left++;
#         }

#         int right = directions.length() - 1;
#         while (right >= 0 && directions.charAt(right) == 'R') {
#             right--;
#         }

#         int collisions = 0;
#         for (int i = left; i <= right; i++) {
#             if (directions.charAt(i) != 'S') {
#                 collisions++;
#             }
#         }

#         return collisions;
#     }
# }

