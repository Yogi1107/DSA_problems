deletions = 0
        b_count = 0

        for ch in s:
            if ch == 'b':
                b_count += 1
            else:  # ch == 'a'
                deletions = min(deletions + 1, b_count)

        return deletions