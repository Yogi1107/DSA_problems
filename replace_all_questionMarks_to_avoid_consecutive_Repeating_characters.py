class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        for i in range(n):
            if s[i] == '?':
                for ch in 'abc':  # 'abc' is enough, 26 not required
                    prev_ok = (i == 0 or s[i - 1] != ch)
                    next_ok = (i == n - 1 or s[i + 1] != ch)
                    if prev_ok and next_ok:
                        s[i] = ch
                        break

        return ''.join(s)
