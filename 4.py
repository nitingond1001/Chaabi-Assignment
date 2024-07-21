# 4Q4. The power of one line -
# Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
# key becomes value. The function's body shouldn't have more than one statement.
# f({
# "key1": "value1",
# "key2": "value2",
# "key3": "value3",
# "key4": "value4",
# "key5": "value5"
# }) should return
# {
# "value1": "key1",
# "value2": "key2",
# "value3": "key3",
# "value4": "key4",
# "value5": "key5"
# }


def func_dict_change(dicts:dict) ->dict:
    return {value:key for key,value in dicts.items()}

print(func_dict_change({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
}))

# Output:
# {'value1': 'key1', 'value2': 'key2', 'value3': 'key3', 'value4': 'key4', 'value5': 'key5'}

