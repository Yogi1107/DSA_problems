n = input()
result = 0
for i, number in enumerate(n[::-1],start=0):
    if number == '1':
        result += 2**i
        i += 1
    else:
        continue

number = int(result)

result_list = []
while number != 0:
    if number % 3 == 0:
        result_list.append('0')
    elif number % 3 == 1:
        result_list.append('1')
    elif number % 3 == 2:
        result_list.append('2')
    else:
        continue
    number = number // 3

result_list.reverse()
result_ = ''.join(result_list)
print(int(result_))
