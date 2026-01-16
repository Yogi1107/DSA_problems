class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        total_days = 0

        for y in range(1971, year):
            total_days += 366 if self.isLeap(y) else 365

        for m in range(month - 1):
            total_days += month_days[m]
            if m == 1 and self.isLeap(year):
                total_days += 1

        total_days += day - 1

        return days[(total_days + 5) % 7]

    def isLeap(self, year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        