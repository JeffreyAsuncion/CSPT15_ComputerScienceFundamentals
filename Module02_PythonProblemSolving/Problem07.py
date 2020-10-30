"""
Given a start integer and an ending integer (both inclusive), 
write a function that returns the count (not the sum) of all integers 
in the range (except integers that contain the digit 5).

Examples:

csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
"""

def csAnythingButFive(start, end):

    # create a list with range
    list_nums = list(range(start, end +1))
    
    # if multip
    result_list = []

    for num  in list_nums:
        str_num = str(num)
        if '5' not in str_num:
            result_list.append(num)


    #return result_list
    return len(result_list)



print(csAnythingButFive(1, 5)) # -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
print(csAnythingButFive(1, 9)) # -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
print(csAnythingButFive(4, 17)) # -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
