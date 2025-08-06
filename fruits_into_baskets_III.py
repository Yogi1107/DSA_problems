#Leet code Questions Solutions. 

#Date : 06/08/2025
#Problem 3479 : Fruits into baskets

from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n, m = len(fruits), len(baskets)
        section = int(m ** 0.5) or 1  
        maxV = [0] * (m // section + 1)

        for i, b in enumerate(baskets):
            maxV[i // section] = max(maxV[i // section], b)

        used = [False] * m
        unplaced = 0

        for fruit in fruits:
            choose = -1
            pos = 0

            while pos < m:
                idx = pos // section

                if maxV[idx] < fruit:
                    pos = (idx + 1) * section
                    continue

                for k in range(pos, min((idx + 1) * section, m)):
                    if not used[k] and baskets[k] >= fruit:
                        choose = k
                        break

                if choose != -1:
                    break
                pos = (idx + 1) * section

            if choose == -1:
                unplaced += 1
            else:
                used[choose] = True

                # Update block's max value after using a basket
                block_start = (choose // section) * section
                block_end = min(block_start + section, m)
                current_max = 0
                for i in range(block_start, block_end):
                    if not used[i]:
                        current_max = max(current_max, baskets[i])
                maxV[choose // section] = current_max

        return unplaced




# The Problem
# You have a list of fruits (fruits[i] = size of the fruit).

# You have baskets (baskets[j] = capacity of the basket).

# Each fruit can only go into one unused basket that is big enough for it.

# If there’s no suitable empty basket for a fruit, that fruit is considered unplaced.

# The code returns the number of unplaced fruits.

# The Idea Behind the Code
# Instead of searching through all baskets one by one for each fruit (which would be slow),
# we split baskets into small groups (blocks) and keep track of the largest basket in each group.
# This way:

# If the biggest basket in a group is too small for a fruit, we skip the whole group at once.

# If it might fit, we only check inside that group.

# This is called square root decomposition — because the group size is about √m.

# Step-by-Step Explanation
# 1. Setup
# python
# Copy
# Edit
# n, m = len(fruits), len(baskets)
# section = int(m ** 0.5) or 1
# maxV = [0] * (m // section + 1)
# section → size of each block (about √m).

# maxV → stores the biggest basket size in each block.

# Example:
# If baskets = [2, 5, 3, 8, 4, 7] and block size = 2
# Then:

# arduino
# Copy
# Edit
# Block 0 → [2, 5] → max = 5
# Block 1 → [3, 8] → max = 8
# Block 2 → [4, 7] → max = 7
# So maxV = [5, 8, 7].

# 2. Precompute block max values
# python
# Copy
# Edit
# for i, b in enumerate(baskets):
#     maxV[i // section] = max(maxV[i // section], b)
# Goes through all baskets and updates maxV for their block.

# 3. Tracking used baskets
# python
# Copy
# Edit
# used = [False] * m
# unplaced = 0
# used[i] is True if basket i is already taken.

# unplaced counts how many fruits can’t be placed.

# 4. Placing each fruit
# python
# Copy
# Edit
# for fruit in fruits:
#     choose = -1
#     pos = 0
# Start looking from the first basket.

# choose will store the chosen basket index for this fruit.

# 5. Searching with block skipping
# python
# Copy
# Edit
# while pos < m:
#     idx = pos // section

#     if maxV[idx] < fruit:
#         pos = (idx + 1) * section
#         continue
# If the largest basket in this block is smaller than the fruit → skip the whole block.

# 6. Checking inside a block
# python
# Copy
# Edit
# for k in range(pos, min((idx + 1) * section, m)):
#     if not used[k] and baskets[k] >= fruit:
#         choose = k
#         break
# Look inside the block for the first unused basket that can fit the fruit.

# 7. Placing or skipping fruit
# python
# Copy
# Edit
# if choose == -1:
#     unplaced += 1
# else:
#     used[choose] = True
# If no basket found → fruit is unplaced.

# If found → mark basket as used.

# 8. Updating block max after using a basket
# python
# Copy
# Edit
# block_start = (choose // section) * section
# block_end = min(block_start + section, m)
# current_max = 0
# for i in range(block_start, block_end):
#     if not used[i]:
#         current_max = max(current_max, baskets[i])
# maxV[choose // section] = current_max
# Once a basket is taken, the maximum size in that block may change.

# Recalculate and update maxV for that block.

# In Short
# Break baskets into √m sized groups.

# Keep track of the biggest basket in each group.

# For each fruit:

# Skip entire groups if their biggest basket is too small.

# If a group might work, check inside it.

# Mark used baskets and update block info.

# Return how many fruits couldn’t be placed.

