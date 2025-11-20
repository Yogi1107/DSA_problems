class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_indices = sorted(range(len(score)), key=lambda i: score[i], reverse=True)
        
        result = [""] * len(score)
        
        for rank, idx in enumerate(sorted_indices):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        
        return result
