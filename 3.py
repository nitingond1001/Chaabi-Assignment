# Q3. Column Sorting, yay!

# Given a list of dicts, write a program to sort the list according to a key given in input.
# E.g.
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "fruit")
# Should Output
# [
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"}
# ]
# AND
# Input f([
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"},
# {"fruit": "blueberry", "color": "blue"}
# ], "color")
# Should Output
# [
# {"fruit": "blueberry", "color": "blue"},
# {"fruit": "orange", "color": "orange"},
# {"fruit": "apple", "color": "red"},
# {"fruit": "banana", "color": "yellow"}
# ]

from functools import cmp_to_key
def keysort_accending_order(x,y):
    return 1 if x["fruit"]>y["fruit"] else -1

def keysort_decending_order(x,y):
    return 1 if x["fruit"]<y["fruit"] else -1
    
new_dict = [{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}]

sortdict = sorted(new_dict, key=cmp_to_key(keysort_accending_order))
second_sortdict = sorted(new_dict, key=cmp_to_key(keysort_decending_order))
print(sortdict)
print(second_sortdict)

# #output :-
# # [{'fruit': 'apple', 'color': 'red'}, {'fruit': 'banana', 'color': 'yellow'}, {'fruit': 'blueberry', 'color': 'blue'}, {'fruit': 'orange', 'color': 'orange'}]
# # [{'fruit': 'orange', 'color': 'orange'}, {'fruit': 'blueberry', 'color': 'blue'}, {'fruit': 'banana', 'color': 'yellow'}, {'fruit': 'apple', 'color': 'red'}]
