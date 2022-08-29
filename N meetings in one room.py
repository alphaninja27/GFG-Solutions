
    def maximumMeetings(self,n,start,end):
        # code here
        ans = []
        for i in range(n):
            ans.append([start[i], end[i]])
        # print(ans)
        ans.sort(key = lambda y : y[1])
        l = 0
        count = 0
        for i in range(n):
            if l < ans[i][0]:
                count += 1
                l = ans[i][1]
        return count
