from collections import defaultdict
class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, n, sum):
        #Your code here
        dicti = defaultdict(lambda: 0)
        ans = 0
        sums = 0
        for i in range(n):
            sums += arr[i]
            if sums == sum:
                ans += 1
            if sums - sum in dicti:
                ans += dicti[sums - sum]
            dicti[sums] += 1
        return ans
