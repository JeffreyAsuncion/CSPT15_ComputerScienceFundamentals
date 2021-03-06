"""
Given a string, write a function that 
returns the index of the first unique (non-repeating) character. 
If there isn't a unique (non-repeating) character, return -1.

Examples:

    csFirstUniqueChar(input_str = "lambdaschool") -> 2
    csFirstUniqueChar(input_str = "ilovelambdaschool") -> 0
    csFirstUniqueChar(input_str = "vvv") -> -1
    Notes:

    input_str will only contain lowercase alpha characters.
    [execution time limit] 4 seconds (py3)

    [input] string input_str

    [output] integer
"""

def csFirstUniqueChar(input_str):
    
    count = {}
    
    # use dict count to Count frequency of letters
    for char in range(len(input_str)):
        if input_str[char] not in count:
            count[input_str[char]] = 1
        else :
            count[input_str[char]] += 1
    
    # search for 1st

    for index, char in enumerate(input_str):
        if count[char] == 1:
            return index
    return -1
            


    
    """
    char_order = []
    count = {}
     
    for char in input_str:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1 
        char_order.append(char)
        
    for index, char in enumerate(input_str):
        if count[char] == 1:
            return index
    return -1
    """


    

print(csFirstUniqueChar(input_str = "lambdaschool")) # -> 2
print(csFirstUniqueChar(input_str = "ilovelambdaschool")) # -> 0
print(csFirstUniqueChar(input_str = "vvv")) # -> -1
