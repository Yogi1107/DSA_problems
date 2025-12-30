class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))

        days_in_month = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        # Check leap year
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days_in_month[1] = 29

        return sum(days_in_month[:month - 1]) + day

# class Solution {
#     public int dayOfYear(String date) {
#         int[] daysInMonth = {
#             31, 28, 31, 30, 31, 30,
#             31, 31, 30, 31, 30, 31
#         };

#         int year = Integer.parseInt(date.substring(0, 4));
#         int month = Integer.parseInt(date.substring(5, 7));
#         int day = Integer.parseInt(date.substring(8, 10));

#         // Check leap year
#         if (isLeapYear(year)) {
#             daysInMonth[1] = 29;
#         }

#         int totalDays = 0;

#         for (int i = 0; i < month - 1; i++) {
#             totalDays += daysInMonth[i];
#         }

#         totalDays += day;

#         return totalDays;
#     }

#     private boolean isLeapYear(int year) {
#         return (year % 400 == 0) ||
#                (year % 4 == 0 && year % 100 != 0);
#     }
# }
