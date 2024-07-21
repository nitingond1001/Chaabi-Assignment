new_dict = {}


def func_dict(string:str, lists: list) -> dict:
    final_dict ={}
    string_pair = string.split(";")
    for strs in string_pair:
        key,value = strs.split(",")
        new_dict[key] = value 

    for string in lists:
        key_value = string.split(".")
        if len(key_value)<=1:
            final_dict[key_value[0]] = new_dict.get(key_value[0], "unknowm")
        else:
            final_dict[string] = new_dict.get(key_value[1], "unknown")
    return final_dict


print(func_dict("xls,spreadsheet;xlsx,spreadsheet;jpg,image", ["abc.jpg",
"xyz.xls", "text.csv", "123"]))

# Output : - 
# {'abc.jpg': 'image', 'xyz.xls': 'spreadsheet', 'text.csv': 'unknown', '123': 'unknowm'}
