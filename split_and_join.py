# #hackerrank Questions Solutions. 

# #Date : 14/08/2025
# #Problem : Split and join

def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

    help(dict)
