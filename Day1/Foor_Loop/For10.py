a=int(raw_input("Enter your first value: "))
b=int(raw_input("Enter your second value: "))
print "First value %d and second value %d "%(a,b) 
for c in range(a,b):
    if(c==2):
        break
    print c
else:
    print "for loop completed"