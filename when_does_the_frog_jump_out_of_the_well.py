def frog_escape_days(height: int, climb: int, slide: int) -> int:
    """
    Calculate the number of days the frog takes to jump out of the well.
    
    Parameters:
    height : int   -> total height of the well
    climb  : int   -> meters frog climbs each day
    slide  : int   -> meters frog slides back each night
    
    Returns:
    int -> total number of days for the frog to escape
    """
    
    # Edge case: frog can climb out in one day
    if climb >= height:
        return 1
    
    # Edge case: frog can never escape
    if climb <= slide:
        return -1  # indicates "never escapes"
    
    days = 0
    current_height = 0
    
    while True:
        days += 1              # start a new day
        current_height += climb  # frog climbs
        
        if current_height >= height:
            # frog escapes the well, do not slide back
            break
        
        # frog slides back at night
        current_height -= slide
    
    return days


# -------------------------------
# Example usage
# -------------------------------
# Example 1: height = 14, climb = 3, slide = 2
print(frog_escape_days(14, 3, 2))  # Output: 12

# Example 2: height = 30, climb = 4, slide = 1
print(frog_escape_days(30, 4, 1))  # Output: 10

# Example 3: edge case: climb >= height
print(frog_escape_days(10, 15, 2))  # Output: 1

# Example 4: edge case: climb <= slide → frog never escapes
print(frog_escape_days(10, 2, 3))   # Output: -1
