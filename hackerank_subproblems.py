# Hackerrank Problems



#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))   

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))




# Enter your code here. Read input from STDIN
n, m = map(int, input().split())  # n must be odd, m = 3*n

# Top half
for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

# Middle line
print("WELCOME".center(m, "-"))

# Bottom half
for i in range(n-2, -1, -2):
    print((".|." * i).center(m, "-"))


## String Formatting

def print_formatted(number):
    # Find the width of the binary representation of the largest number
    width = len(bin(number)[2:])
    
    for i in range(1, number+1):
        # Each value should be right-aligned within 'width'
        print(str(i).rjust(width),
              oct(i)[2:].rjust(width),
              hex(i)[2:].upper().rjust(width),
              bin(i)[2:].rjust(width))
            
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)