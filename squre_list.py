list =[[4,6,7,4],[2,4,6],[2,6,9]]
i=0
while i<len(list):
    j=0
    while j < len(list[j]):
        j=j+1
        if len(list[i]) == len(list[j]):
            print "squre hai"
        else:
            print "not squre"
        j=j+1
    i=i+1