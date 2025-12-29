class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        from collections import defaultdict

        # Build mapping: pair -> possible tops
        patterns = defaultdict(list)
        for a, b, c in allowed:
            patterns[a + b].append(c)

        memo = {}

        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True

            if row in memo:
                return memo[row]

            # Generate next row using backtracking
            def build_next(i: int, next_row: list) -> bool:
                if i == len(row) - 1:
                    return dfs("".join(next_row))

                pair = row[i] + row[i + 1]
                if pair not in patterns:
                    return False

                for ch in patterns[pair]:
                    next_row.append(ch)
                    if build_next(i + 1, next_row):
                        return True
                    next_row.pop()

                return False

            memo[row] = build_next(0, [])
            return memo[row]

        return dfs(bottom)
