
# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

def func_string_set(lists1:list, lists2:list) -> list:
    return list(set(lists1).intersection(lists2)), list(set(lists1).symmetric_difference(lists2))

mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword \
Art Online","Bleach","Dragon Ball Z","One Piece"] 
must_watch = ["Full Metal Alchemist","Code Geass","Death \
Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack \
On Titan"]
comman , notcomman = func_string_set(mainstream, must_watch)
print(comman)
print(notcomman)

# output:
# ['Attack On Titan', 'One Piece']
# ['Bleach', 'One Punch Man', 'Sword Art Online', "Stein's Gate", 'Death Note', 'Dragon Ball Z', 'The Devil is a Part Timer!', 'Full Metal Alchemist', 'Code Geass']
