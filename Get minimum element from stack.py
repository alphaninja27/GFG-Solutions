class stack:
    def __init__(self):
        self.s=[]
        self.minEle=None

    def push(self,x):
        #CODE HERE
        self.s.append(x)

    def pop(self):
        #CODE HERE
        if self.s:
            return self.s.pop()
        else:
            return -1
        

    def getMin(self):
        #CODE HERE
        maxi = 1000000
        if self.s:
            for i in self.s:
                maxi = min(i, maxi)
            return maxi
        else:
            return -1
