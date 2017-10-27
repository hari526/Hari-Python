#target=['a','s','a','sl']
#def remove_duplicates(source):
#    for element in source:
 #       if element not in target:
 #           target.append(element)
#    return target
#print(target)

#remove_duplicates(['a','s','f','a','a'])

def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)
            print('target',target)
    return target
remove_duplicates(['s','aa','sss','kk','kk','kk','kk'])
#len(target)
#print(tet)
#print(target)
