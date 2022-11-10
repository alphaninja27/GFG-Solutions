class Solution:
	def NthRoot(self, n, m):
		# Code here
		l = 0
		h = m
		mid = 0
		while l <= h:
		    mid = (l + h) // 2
		    t = pow(mid, n)
		    if t == m:
		        return mid
		    if t < m:
		        l = mid + 1
		    else:
		        h = mid - 1
		return -1
