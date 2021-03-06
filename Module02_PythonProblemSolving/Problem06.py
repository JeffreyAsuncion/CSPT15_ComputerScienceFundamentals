"""
Given two strings that include only lowercase alpha characters, str_1 and str_2, write a function that 
returns a new sorted string that contains any character (only once) that appeared in str_1 or str_2.

Examples:

csLongestPossible("aabbbcccdef", "xxyyzzz") -> "abcdefxyz"
csLongestPossible("abc", "abc") -> "abc"
[execution time limit] 4 seconds (py3)

[input] string str_1

[input] string str_2

[output] string
"""



def csLongestPossible(str_1, str_2):

    newStr= str_1 + str_2
    
    uniqueStr="" 
    for letter in newStr: 
        if(letter in uniqueStr): 
            pass
        else: 
            uniqueStr=uniqueStr+letter 
    
    uniqueStr = sorted(uniqueStr)
    resultStr = "".join(uniqueStr)
    
    return resultStr 



print(csLongestPossible("aabbbcccdef", "xxyyzzz")) # -> "abcdefxyz"
print(csLongestPossible("abc", "abc")) # -> "abc"
