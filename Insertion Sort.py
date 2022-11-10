class Solution:
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        key = 0
        j = 0
        for i in range(n):
            key = alist[i]
            j = i - 1
            while j >= 0 and alist[j] > key:
                alist[j + 1] = alist[j]
                j = j - 1
            alist[j + 1] = key
        return alist 
