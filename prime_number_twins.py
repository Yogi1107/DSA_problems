
def is_Prime(n):
    if n == 0 or n == 1:
        return 0
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return 0
                
    return 1
    
n = 50
d = {}
for i in range(1,n):
    if is_Prime(i) and is_Prime(i+6):
        d[i] = i + 6
    
print(d)
