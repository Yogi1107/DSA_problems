array = [1,1,1,2,2,3,3,3]
result = []
for i in array:
    if i not in result:
        result.append(i)

print("Total unique numbers:- ",len(result))
print("Result list: ",result)

# print("Result array:- ",set(array))
# this is not inplace


# do usng two loops considering the variables count and key

