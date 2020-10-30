"""
Given an array of integers, return the sum of all the positive integers in the array.

Examples:

csSumOfPositive([1, 2, 3, -4, 5]) -> 1 + 2 + 3 + 5 = 11
csSumOfPositive([-3, -2, -1, 0, 1]) -> 1
csSumOfPositive([-3, -2]) -> 0
Notes:

If the input_arr does not contain any positive integers, the default sum should be 0.
[execution time limit] 4 seconds (py3)

[input] array.integer input_arr

[output] integer
"""


def csSumOfPositive(input_arr):
    # Given a list of ints
    sumPositiveNums = 0

    # cycle thru list of int
    for num in input_arr:
        # check if num > 0
        if num > 0:
            # add to sumPositiveNums
            sumPositiveNums += num
    # int return the sum of all positive ints 
    return sumPositiveNums



print(csSumOfPositive([1, 2, 3, -4, 5])) # -> 1 + 2 + 3 + 5 = 11
print(csSumOfPositive([-3, -2, -1, 0, 1])) # -> 1
print(csSumOfPositive([-3, -2])) # -> 0