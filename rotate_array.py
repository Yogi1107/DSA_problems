size = int(input("Enter the size of the array:- "))
array = []
for i in range(size):
    element = int(input(f"Enter the element {i+1}:- "))
    array.append(i)

print("Original Array:- ",array)

index = int(input("Enter the index from which array is to be rotated."))
result_array = []
for i in range(index-1,len(array)):
    result_array.append(i)

for i in array:
    if i not in result_array:
        result_array.append(i)

print("Result array:- ",result_array)

# try always swapping when it comes rotating the array
