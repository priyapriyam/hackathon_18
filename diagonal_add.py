list=[[5,6,8],[9,2,4],[9,7,9]]
sum1=0
sum2=0
j=-1
i=0
while i<len(list):
    sum1=sum1+list[i][i]
    sum2=sum2+list[i][j]
    j=j-1
    i=i+1
print sum1
print sum2