class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        tot = 0
        dp = [0] * 26

        for c in s:
            idx = ord(c) - 97
            new = (tot + 1 - dp[idx]) % MOD
            tot = (tot + new) % MOD
            dp[idx] = (dp[idx] + new) % MOD

        return tot