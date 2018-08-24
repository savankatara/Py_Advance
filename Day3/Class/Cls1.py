class Cls1:
    
    'python program with class and function'
    def __init__(self):
        print "non paramaterized constructer"
        
    def getprint(self,name):
        print "name : ",name
c1=Cls1()
c1.getprint(name="savan")
print Cls1.__doc__
print Cls1.__name__

print Cls1.__dict__
print Cls1.__module__

print Cls1.__bases__