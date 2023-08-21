#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,N):
        # code here 
        a = [0] * N
        b = [0] * N
        a[0] = b[0] = 1
        for i in range(1, N):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]
        return (1 << N) - a[N - 1] - b[N - 1]
