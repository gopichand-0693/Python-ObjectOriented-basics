
#In this module we will look into few algorithms

# selection sort

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


# Insertion sort

data = [-2, 45, 0, 11, -9]

for i in range(1, len(data)):
    j = i - 1
    while j >= 0:
        if data[i] < data[j]:
            data[i], data[j] = data[j], data[i]
        j -= 1
        i -= 1

print(data)

assert(data == lis)
