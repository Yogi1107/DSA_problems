n = int(input("Enter the number:- "))
result = []
while n != 0:
    if n % 2 == 0:
        result.append('0')
    elif n % 2 == 1:
        result.append('1')
    else:
        continue
    n = n // 2

result.reverse()
result_ = ''.join(result)
print(result_)