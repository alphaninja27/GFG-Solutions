def maxSquare(self, n, m, mat):
        # code here
        ans = [[-1] * m for i in range(n)]
        l = max(max([mat[i][0] for i in range(n)]), max([mat[0][i] for i in range(m)]))
        for i in range(n):
            ans[i][0] = mat[i][0]
        for i in range(m):
            ans[0][i] = mat[0][i]
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][j] == 1:
                    ans[i][j] = min(ans[i - 1][j], ans[i][j - 1], ans[i - 1][j - 1]) + 1
                    l = max(l, ans[i][j])
                else:
                    ans[i][j] = 0
        return l
