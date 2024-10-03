def highest_in_sublist():
 list10=[[8,10,2],[6,18,24],[26,13,39],[28,14]]
 print ("SORTED LIST - ")
 for sublist in list10:
    sublist.sort()
 print (list10)
 print ("SECOND HIGHEST IN SUBLIST - ")
 for sublist in list10:
    print (sublist[-2])

highest_in_sublist()

def second_highest_in_list():
    list1=[[8,10,2],[24,6,18],[39,13,26],[28,14]]
    #SORTED LIST
    for val in list1:
        val.sort()
    print (list1)
    l1=[]
    for inner in list1:
        l1.append(inner[-2])
    return l1
    #print (list1)

    #for val in list1:
        #print (val[-2])

res=second_highest_in_list()
print (f'Second highest -> {res}')
