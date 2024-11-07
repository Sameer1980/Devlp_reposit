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