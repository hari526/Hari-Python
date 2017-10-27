def binaryrSearch(myItem,myList):
    found= False
    bottom = 0
    top = len(myList)-1
    while bottom <= top and not found:
	middle = ((bottom+top)//2)
	if myList[middle]==myitem:
		found = True
	elif myList[middle] < myitem:
		bottom = middle + 1
	elif myList[middle] > myitem:
		top = middle - 1
    return found
			


if __name__== "__main__":
    numbers_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    item = int(input( "what item do you want to search : "))
    isitFound = binaryrSearch(item,numbers_list)
    if isitFound:
        print("Item is in the list !")
    else:
        print("Item is not in the list !")
