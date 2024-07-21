# '''Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]
# '''


# # Solution 

def selection_sorting(array: list) -> list:
    for index in range(len(array)):
        min_index = index
 
        for j in range(index + 1, len(array)):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        array[index], array[min_index] = array[min_index], array[index]
    return array

input = selection_sorting([5,416,54,21,6135,15,741])
print(input) # output is [5, 15, 21, 54, 416, 741, 6135]