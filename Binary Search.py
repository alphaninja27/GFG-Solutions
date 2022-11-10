class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		l = 0
		r = len(arr) - 1
		mid = 0
		while l <= r:
		    mid = l + (r - l) // 2
		    if arr[mid] == k:
		        return mid
		    elif arr[mid] < k:
		        l = mid + 1
		    else:
		        r = mid - 1
		return -1
