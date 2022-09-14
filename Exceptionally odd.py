class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        ans = 0
        for i in arr:
            ans = ans ^ i
        return ans
