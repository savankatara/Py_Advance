a=int(raw_input("Enter your first value: "))
b=int(raw_input("Enter your second value: "))
print "First value %d and second value %d "%(a,b) 
for c in range(a,b):
    for e in range(c,5):
        print e
    
    if(c==2):
        pass
        print "pass working"
    print c
else:
    print "for loop completed"