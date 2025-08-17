#lettcode Problem

#date : 17/08/2025
#Problem : 1002 : Common Character

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
    
        for word in words[1:]:
            common &= Counter(word)   
        
        result = []
        for char, count in common.items():
            result.extend([char] * count)
    
        return result
        
		
# class Solution:
#     def commonChars(self, words: List[str]) -> List[str]:
#         common_chars = set(words[0])
        
#         for word in words[1:]:
#             common_chars &= set(word)
            
#         result = []
#         for char in common_chars:
#             min_count = min(word.count(char) for word in words)
#             result.extend([char] * min_count)
            
#         return result    
            
        