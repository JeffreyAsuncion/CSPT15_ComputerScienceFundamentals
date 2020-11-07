"""
Given a string, 
write a function that removes all duplicate words from the input. 
The string that you return should only contain the first occurrence of each word in the string.

Examples:

`csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta") -> "alpha bravo golf delta"
`csRemoveDuplicateWords("my dog is my dog is super smart") -> "my dog is super smart"
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
"""



"""
    # take in string
    # split string into list of words using .split(" ")

    # intialize dictionary to count word appearance
    # initialize a result string var
    # iterate thru list of words
        # if the word is NOT present in the dict
            # add the word to the result string
            # add the word to the dict
        # otherwise
            # add + 1 to the word to the dictionary
    # return the result string # clean the trailing " "
"""

def csRemoveDuplicateWords(input_str):
    # take in string
    # split string into list of words using .split(" ")
    lst_words = input_str.split(" ")
    # intialize dictionary to count word appearance
    my_dict = {}
    # initialize a result string var
    result_str = ""
    # iterate thru list of words
    for word in lst_words:
        # if the word is NOT present in the dict
        if word not in my_dict:
            # add the word to the result string
            result_str += word + " "
            my_dict[word] = 1
        # otherwise
        else:
            # add the word to the dictionary
            my_dict[word] += 1
    # return the result string
    return result_str[:-1] # clean trailing " "



print(csRemoveDuplicateWords("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta"))# -> "alpha bravo golf delta"
print(csRemoveDuplicateWords("my dog is my dog is super smart"))# -> "my dog is super smart"
#[execution time limit] 4 seconds (py3)