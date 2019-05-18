list=[3,5,4,7,9]
list1=[2,3,6,4,5]
i=0
new=[]
while i<len(list):
    if list[i] not in list1:
    	new.append(list[i])       
    i=i+1
print new