class Solution:
    def pyramidTransition(self, bottom: str, allowed: list[str]) -> bool:
        from collections import defaultdict

        # Build mapping: "AB" -> ["C", "D", ...]
        patterns = defaultdict(list)
        for a, b, c in allowed:
            patterns[a + b].append(c)

        # DFS to build pyramid
        def dfs(curr: str) -> bool:
            if len(curr) == 1:
                return True

            # Try to build next row
            def backtrack(i: int, next_row: list) -> bool:
                if i == len(curr) - 1:
                    return dfs("".join(next_row))

                pair = curr[i] + curr[i + 1]
                if pair not in patterns:
                    return False

                for ch in patterns[pair]:
                    next_row.append(ch)
                    if backtrack(i + 1, next_row):
                        return True
                    next_row.pop()

                return False

            return backtrack(0, [])

        return dfs(bottom)
