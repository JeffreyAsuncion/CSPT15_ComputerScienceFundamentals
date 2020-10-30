"""
Given a string, return a new string with all the vowels removed.

Examples:

csRemoveTheVowels("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] string
"""

def csRemoveTheVowels(input_str):
    
    
    # make a list of vowels upper and lower case
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    
    # make a new str
    new_str = ""
    
    # for each letter in input_str
    for letter in input_str:
        # check if it is a vowel dont add
        if letter in vowels:
            new_str = new_str
        # not a vowel then add to new_str
        else:
            new_str += letter
    # don't forget to return a value
    return new_str
    

print(csRemoveTheVowels("Lambda School is awesome!")) #-> "Lmbd Schl s wsm!"