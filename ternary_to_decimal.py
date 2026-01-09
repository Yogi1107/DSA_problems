n = input()
result = 0
for i, number in enumerate(n[::-1],start=0):
    if number == '1':
        result += 3**i
    elif number == '2':
        result += 3**i*2
    else:
        continue

print(result)