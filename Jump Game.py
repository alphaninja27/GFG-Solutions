class Solution:
    def canReach(self, A, N):
        # code here
        reach = 0
        for i in range(N):
            if i > reach:
                return 0
            reach = max(reach, A[i] + i)
        return 1
