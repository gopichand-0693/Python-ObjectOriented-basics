
# In this module we will look into few algorithms

"""
Sorting algorithms
"""

#  Basic linear search


def linear_search(arr, x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i


linear_search([1,3,4,2,5,6,3,1], 6)


"""
Sorting algorithms
"""

# selection sort


def selection_sort(arr):
    lis = arr
    for i in range(0, len(lis)):
        min=lis[i]
        min_index=i
        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_index]:
                min_index=j
                min = lis[j]
        lis[i], lis[min_index]=min, lis[i]


lis = [-2, 45, 0, 11, -9]  # [3,4,5,1,6,2]
selection_sort(lis)
print(lis)


# Insertion sort

def insertion_sort(arr):
    arr = data
    for i in range(1, len(data)):
        j = i - 1
        while j >= 0:
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
            j -= 1
            i -= 1


data = [-2, 45, 0, 11, -9]
insertion_sort(data)
print(data)

assert(data == lis)


def merge_sort(arr):

    if len(arr) > 1:
        mid_point = len(arr)//2
        left = arr[:mid_point]
        right = arr[mid_point:]

        merge_sort(left)
        merge_sort(right)

            # l [1,2,3,5] r [4,5,6,7,8]
        i, j, k = 0, 0, 0
        l = left
        r = right
        while i < len(l) and j < len(r) :
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
        return arr


array = [-2, 45, 0, 11, -9]
merge_sort(array)
print(array)