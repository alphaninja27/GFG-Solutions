#User function Template for python3

class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        dp = [[0] * N for _ in range(N)]
        dp[N - 1] = Matrix[N - 1]
        for r in range(N - 2, -1, -1):
            for c in range(N - 1, -1, -1):
                l_d = 0 if c == 0 else dp[r + 1][c - 1]
                d = dp[r + 1][c]
                r_d = 0 if c == N - 1 else dp[r + 1][c + 1]
                dp[r][c] = Matrix[r][c] + max(l_d, d, r_d)
        return max(dp[0])
