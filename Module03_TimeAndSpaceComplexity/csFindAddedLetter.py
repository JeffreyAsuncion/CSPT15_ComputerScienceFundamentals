"""
You are given two strings, str_1 and str_2, 
where str_2 is generated by randomly shuffling str_1 
and then adding one letter at a random position.

Write a function that returns the letter that was added to str_2.

Examples:

    csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef") -> "f"
    csFindAddedLetter(str_1 = "", str_2 = "z") -> "z"
    csFindAddedLetter(str_1 = "b", str_2 = "bb") -> "b"
    csFindAddedLetter(str_1 = "bf", str_2 = "bfb") -> "b"
    Notes:

    str_1 and str_2 both consist of only lowercase alpha characters.
    [execution time limit] 4 seconds (py3)

    [input] string str_1

    [input] string str_2

    [output] string
"""

def csFindAddedLetter(str_1, str_2):
    if str_1 == "":
        return str_2

    lst_1 = sorted(str_1)
    # to even out the lists
    lst_1.append(" ")
    lst_2 = sorted(str_2)
                                    
    for i in range(len(lst_2)+1):
                                             
        if lst_1[i] != lst_2[i]:
            return lst_2[i]




print(csFindAddedLetter(str_1 = "bcde", str_2 = "bcdef")) # -> "f"
print(csFindAddedLetter(str_1 = "", str_2 = "z")) # -> "z"
print(csFindAddedLetter(str_1 = "b", str_2 = "bb")) # -> "b"
print(csFindAddedLetter(str_1 = "bf", str_2 = "bfb")) # -> "b"

