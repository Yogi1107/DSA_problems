class Solution:
    def reformatDate(self, date: str) -> str:
        parts = date.split()

        day_part = parts[0]
        month_part = parts[1]
        year_part = parts[2]

        # Extract numeric day (remove suffix)
        day_number = ""
        for ch in day_part:
            if ch.isdigit():
                day_number += ch

        if len(day_number) == 1:
            day_number = "0" + day_number

        # Map month to number 
        month_map = {
            "Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"
        }
        
        month_number = month_map[month_part]
        return year_part + "-" + month_number + "-" + day_number
