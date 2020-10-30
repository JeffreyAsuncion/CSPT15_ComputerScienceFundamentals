"""
Given a string of words, return the length of the shortest word(s).

Notes:

The input string will never be empty and you do not need to validate for different data types.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] integer
"""

def csShortestWord(input_str):

    # replace escape characters
    input_str = input_str.replace("\n", " ")
    input_str = input_str.replace("\t", " ")
    # take input str and split into words
    list = input_str.split(" ")

    lenShortestWord = 1000000
    # cycle thru list of words
    for word in list:
        if len(word) < lenShortestWord:
            lenShortestWord = len(word)


    return lenShortestWord 


print(csShortestWord("ZxuvWBoofsTUtasPIhsuCJjttHhBuuHZoxZk\tWZxAkjdCqDpML"))
