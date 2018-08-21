a=10
b=20
if(a==10):
    print "True condition"
    if(b==20):
    #elif(a==12):
        print "a==20"
    elif(a==11):
        print "a==11"
    elif(a==10):
        print "a==10"
    elif(a==9):
        print "a==9"
    else:
        print "false inner else"
else:
    print "False condition"