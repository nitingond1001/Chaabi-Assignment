# Q6. Every other sub-list
# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

def func_sub_list(lists:list, start:int, end:int) -> list:
    return list(filter(lambda a: a%2==1, lists[start:end+1:2]))

print(func_sub_list([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9))

# # output:
# # [5,11,17,23]