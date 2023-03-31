class Solution:
	def subsetSums(self, arr, N):
		# code here
		def helper(ind,s):
		    if(ind==N):
		        res.append(s)
		        return
		    helper(ind+1,s+arr[ind])
		    helper(ind+1,s)
		    
		s=0
		res=[]
		helper(0,s)
        return res
