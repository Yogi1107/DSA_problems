n = input()
result = 0
for i, number in enumerate(n[::-1],start=0):
    if number == '1':
        result += 2**i
        i += 1
    else:
        continue
print(result)
