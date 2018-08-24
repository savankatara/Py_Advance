class Cls1:
    
    'python program with class and function'
    def __init__(self,name ,rollnum):
        self.name=name
        self.rollnum=rollnum
    def Display(self):
        print "name : ",self.name,"RollNumber : ",self.rollnum
       
c1=Cls1(name="savan",rollnum=101)
c2=Cls1(name="python",rollnum=102)
c1.Display()
c2.Display()