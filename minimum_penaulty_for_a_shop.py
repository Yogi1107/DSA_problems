class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')  # closing at hour 0
        min_penalty = penalty
        best_hour = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1   # one less Y in suffix
            else:
                penalty += 1   # one more N in prefix

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1

        return best_hour
