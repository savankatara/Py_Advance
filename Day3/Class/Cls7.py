class Cls1:
    
    'python program with class and function'
    def __init__(self,n ,r):
        self.n1=n
        self.r1=r
    def getprint(self):
        print "{0}+{1}j".format(self.n1, self.r1)
c1=Cls1(10,20)
c1.getprint()
