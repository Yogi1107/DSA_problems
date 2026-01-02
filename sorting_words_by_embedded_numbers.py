string = input("Enter a string: ")

words = string.split()
temp = []

# Extract digit and word
for word in words:
    for char in word:
        if char.isdigit():
            temp.append((int(char), word))
            break

# Sort by digit
temp.sort()

# Remove digits and form result
result = []
for _, word in temp:
    cleaned_word = ""
    for char in word:
        if not char.isdigit():
            cleaned_word += char
    result.append(cleaned_word)

print(" ".join(result))
