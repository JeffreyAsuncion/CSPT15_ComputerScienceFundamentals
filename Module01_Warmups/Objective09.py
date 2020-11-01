"""
    Objective 09 - Evaluate conditional expressions and use boolean operators to control flow
"""


"""
    Change the assignment statements below so that all of the print functions call print True
"""

# change these values so that all of the print statements print True
number = 20 # 10
second_number = 0 # 10
first_list = [1, 1, 1] # []
second_list = [1, 2]   # [1, 2, 3]
# only change the code above this line

# all of these print statements must print True by only changing the assignment statementss above 
print(number > 15)
print(first_list)
print(len(second_list)==2)
print(len(first_list)+len(second_list) == 5)
print(first_list and first_list[0] == 1)
print(not second_number)
