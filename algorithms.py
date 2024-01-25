
#In this module we will look into few algorithms

# Insertion sort

lis =  [-2, 45, 0, 11, -9] # [3,4,5,1,6,2]

for i in range(0, len(lis)):
    min=lis[i]
    min_index=i
    for j in range(i+1, len(lis)):
        if lis[j] < lis[min_index]:
            min_index=j
            min = lis[j]
    lis[i], lis[min_index]=min, lis[i]
print(lis)


