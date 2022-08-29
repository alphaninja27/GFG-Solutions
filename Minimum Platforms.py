def minimumPlatform(self,n,arr,dep):
        # code here
        maxx=dep[n-1]
        time=[0]*(2361)
        
        for i in range(n):
            time[arr[i]]+=1
            time[dep[i]+1]-=1
        maxx=0
        for i in range(1,len(time)):
            time[i]=time[i-1]+time[i]
            if time[i]>maxx:
                maxx=time[i]
        return maxx 
