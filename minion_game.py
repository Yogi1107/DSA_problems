def minion_game(s):
    s = s.upper()  # Ensure uppercase
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(s)
    
    for i in range(n):
        if s[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
