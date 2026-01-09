n = int(input("Enter the number:- "))
result = []
while n != 0:
    if n % 3 == 0:
        result.append('0')
    elif n % 3 == 1:
        result.append('1')
    elif n % 3 == 2:
        result.append('2')
    else:
        continue
    n = n // 3

result.reverse()
result_ = ''.join(result)
print(result_)