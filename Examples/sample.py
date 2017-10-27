def nearest_square(l):
    s=0
    n=0
    while(n*n<=l):
        s=(n*n)
        return s
        n=n+1
        
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))

