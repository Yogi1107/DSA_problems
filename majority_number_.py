array = [1,1,1,2,2,2,2,3,3]
# count = [0 for _ in range(max(array))]
# for i in array:
#     count[i-1] += 1

# print(count)

# print("Majority Element:- ",array[])

result = {}
for i in array:
    result[i] = array.count(i)

print(result)

max_ = result[1]
element = 1
for i in result.keys():
    if result[i] > max_:
        max_ = result[i]
        element = i

print("Majority Element is:- ",element)

# do using two loops considering the variables count and key
