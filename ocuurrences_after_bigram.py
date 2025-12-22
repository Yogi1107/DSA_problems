class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        str_list = text.split()
        result = []
        for i in range(2,len(str_list)):
            if str_list[i-2] == first and str_list[i-1] == second:
                result.append(str_list[i])

        return result
        
