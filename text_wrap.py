#HAckerank Problem
#Text Wrap

#Date : 23rd Aug 2025
import textwrap

def wrap(string, max_width):
    result = ""
    for i in range(0, len(string), max_width):  # step through in chunks
        result += string[i:i+max_width] + "\n"
    return result.strip()  # remove last newline
    
# import textwrap

# def wrap(string, max_width):
#     return "\n".join(textwrap.wrap(string, max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)