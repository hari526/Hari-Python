#TODO: Implement the nearest_square function
def nearest_square(limit):
    num=1
    square=num*num
    while(square < limit):
        print(square)
        print(num)
        square=num*num
        num=num+1
        return square
    
test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
