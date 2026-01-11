# Function to count leap years up to year Y
def count_leap_years(year):
    """
    Counts the number of leap years from year 1 to the given year.
    Leap year rules:
        - divisible by 4 → leap year
        - divisible by 100 → not a leap year
        - divisible by 400 → leap year
    """
    return (year // 4) - (year // 100) + (year // 400)


# Input dates in DD-MM-YYYY format
date1 = input("Enter the first date (DD-MM-YYYY): ")
date2 = input("Enter the second date (DD-MM-YYYY): ")

# Split the dates into day, month, year and convert to integers
d1, m1, y1 = map(int, date1.split('-'))
d2, m2, y2 = map(int, date2.split('-'))

# Days in each month (non-leap year)
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# -------------------------------
# Step 1: Calculate remaining days in start year (from date1 to Dec 31)
# -------------------------------
# Days remaining in the current month
days_from_start_year = month_days[m1 - 1] - d1 + 1

# Add days from remaining months
for i in range(m1, 12):
    days_from_start_year += month_days[i]

# If start year is a leap year and month is Jan or Feb, add 1 extra day
if (y1 % 400 == 0 or (y1 % 100 != 0 and y1 % 4 == 0)) and m1 <= 2:
    days_from_start_year += 1

# -------------------------------
# Step 2: Calculate days in end year (from Jan 1 to date2)
# -------------------------------
days_from_end_year = sum(month_days[:m2 - 1]) + d2

# If end year is a leap year and month is after Feb, add 1 extra day
if (y2 % 400 == 0 or (y2 % 100 != 0 and y2 % 4 == 0)) and m2 > 2:
    days_from_end_year += 1

# -------------------------------
# Step 3: Calculate days in full years in between (excluding start and end years)
# -------------------------------
full_years = y2 - y1 - 1  # Number of full years between start and end
days_in_full_years = full_years * 365

# -------------------------------
# Step 4: Calculate leap days in the full years in between
# -------------------------------
# Count leap years up to end year - 1 and start year
leap_days_in_between = count_leap_years(y2 - 1) - count_leap_years(y1)

# -------------------------------
# Step 5: Combine everything to get total days
# -------------------------------
total_days = days_from_start_year + days_from_end_year + days_in_full_years + leap_days_in_between

# Output
print(f"Number of days between {date1} and {date2} (inclusive): {total_days}")
