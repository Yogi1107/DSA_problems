def count_sort(arr):
    """
    Sorts an array of non-negative integers using the Counting Sort algorithm.
    """
    if not arr:
        return []

    # 1. Determine the range (k)
    # k is the max value + 1 to account for 0
    k = max(arr) + 1
    n = len(arr)

    # 2. Initialize the Count array (c) and the Output array (b)
    # c: size k, initialized to 0
    # b: size n, initialized to 0 (or None)
    c = [0] * k
    b = [0] * n 
    
    

    # 3. Store the count of each element
    for x in arr:
        c[x] += 1

    # 4. Store the cumulative count (Prefix Sum)
    # c[i] now contains the actual position (index + 1) of the last occurrence of element i 
    for i in range(1, k):
        c[i] += c[i-1]

    # 5. Place the elements into the output array (b)
    # Iterate backwards to ensure stability (for elements with the same key)
    # The loop should go from index n-1 down to 0
    for i in range(n - 1, -1, -1):
        # The correct 0-indexed position is c[arr[i]] - 1
        element = arr[i]
        position = c[element] - 1
        b[position] = element
        # Decrease the count for the next identical element
        c[element] -= 1

    # 6. Copy the sorted elements back to the original array (or return b)
    # The original implementation copied back, so we'll do the same for clarity, 
    # but returning b is more standard.
    # for i in range(n):
    #     arr[i] = b[i]
    
    return b

# --- Main Program ---
# Use a try-except block to handle potential non-integer input
while True:
    try:
        n = int(input("Enter the number of elements: "))
        if n < 0:
            print("Please enter a non-negative number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

arr = []
for i in range(n):
    while True:
        try:
            element = int(input(f"Enter the element {i} (non-negative integer): "))
            if element < 0:
                 print("Counting Sort works best for non-negative integers. Please enter a non-negative number.")
                 continue
            arr.append(element) # Corrected: append the element, not the index
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

print("\nOriginal Array:", arr)

# Call the corrected function
result_array = count_sort(arr)

print("Count Sorted Array:", result_array)