class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def tribo(n):
            if n in memo:
                return memo[n]
            if n == 0:
                result = 0
            elif n == 1 or n == 2:
                result = 1
            else:
                result = tribo(n - 1) + tribo(n - 2) + tribo(n - 3)
                memo[n] = result
            return result

        return tribo(n)
