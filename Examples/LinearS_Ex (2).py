def linearSearch(myItem,myList):
    found= False
    position=0
    counter=0
    while position < len(myList) and not found:
        if myList[position]== myItem:
            found = True
        counter+=1
        position= position+1
    print("The counter is : ",counter)
    return found
    

if __name__== "__main__":
    shopping = ["apples","bananas","chocolate","pasta"]
    item = input( "what item do you want to search : ")
    isitFound = linearSearch(item,shopping)
    if isitFound:
        print("Item is in the list !")
    else:
        print("Item is not in the list !")
        shopping.append(item)
        print("The  new list : ",shopping)
