class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        if n == 1:
            return "1"
        arr = [1, 1]
        if n == 2:
            return arr
        else:
            for i in range(n - 2):
                nxt = arr[i] + arr[i + 1]
                arr.append(nxt)
            return arr
