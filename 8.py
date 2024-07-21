# Q8. Some neat tricks up her sleeve:
# Looking at the below code, write down the final values of A0, A1, ...An
from functools import reduce
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = list(map(lambda x: x*2, [1,2,3,4]))
A9 = filter(lambda x: len(x) >3, ["I" , "want", "to", "learn", "python"]) # if 
# we use list in the A9 then the output is :
A10 = list(A9)

print(A0,A1,A3,A4,A5,A6,A7,A8,A10, end="\n")

# # Output:

# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
# range(0, 10)
# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
# 21 
# <map object at 0x000001E9F6133DC0> <filter object at 0x000001E9F6133D30>
# ["want","learn","python"]