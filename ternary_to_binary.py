n = input()
result =  0
for i, number in enumerate(n[::-1], start=0):
    if number == '1':
        result += 3**i
    elif number == '2':
        result += 3**i*2
    else:
        continue

number_decimal = int(result)

resuklt_ternary = []
while number_decimal > 0:
    if number_decimal % 2 == 1:
        resuklt_ternary.append('1')
    elif number_decimal % 2 == 0:
        resuklt_ternary.append('0')
    else:
        continue
    number_decimal = number_decimal//2

result_ternary_number = ''.join(resuklt_ternary)
print(result_ternary_number)