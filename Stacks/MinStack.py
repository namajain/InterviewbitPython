class MinStack:
    # @param x, an integer
    def __init__(self):
        self.a =[]
        self.m = None

    def push(self, x):

        if self.m is None or x < self.m:
            y = (2 * x - self.m) if self.m else x
            self.m = x
            self.a.append(y)
        else:
            self.a.append(x)
        # print '\n push ' + str(x)
        # print self.a

    # @return nothing
    def pop(self):

        if not self.a:
            # print '\nempty'
            return -1
        x = self.a.pop()
        # print '\npop'
        # print self.a

        if x < self.m:
            p = self.m
            y = 2 * self.m - x
            self.m = y
            if not self.a:
                self.m = None
            return p
        if not self.a:
            self.m = None
        return x

    # @return an integer
    def top(self):
        # print '\npeek'
        if not self.a:
            return -1
        x = self.a[-1]
        return max(x,self.m)

    # @return an integer
    def getMin(self):
        # print '\nmin'
        if not self.a:
            return -1
        return self.m

