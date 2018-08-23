a=(10,20,50,50.,"hey")
b=('world',"python")
c=a + b
print c
print a
del a
print a
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print tup3
