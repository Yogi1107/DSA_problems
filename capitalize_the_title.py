#leetcode problem
#Problem 2129: Capitalize the title
#Date: 16-09-2025


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_list = title.split()
        result = []
        for i in title_list:
            if len(i) <= 2:
                result.append(i.lower())
            else:
                result.append(i.capitalize())
        result_str = " ".join(result)
        return result_str
