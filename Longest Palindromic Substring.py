class Solution:
    def longestPalindrome(self, S):
        # code here
        l = [S[i:j] for i in range(len(S)) for j in range(i + 1, len(S) + 1)]
        m = []
        for i in l:
            if i == i[::-1]:
                m.append(i)
        return max(m, key = len)
