#Count the frequency of each element in a list.

list=[1,1,2,3,4,2,3,7]

fr=[]

for i in list:
    count=0
    for j in list:
        if i==j:
            count+=1

if i not in list[:list.index(i)]:
        print(i,"appers",count,"times")

    



