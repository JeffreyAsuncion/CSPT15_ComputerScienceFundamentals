"""
    Objective 08 - Perform basic string operations
"""



"""
    Modify the "mystery_string" below until all of the print statements 
    print as expected based on the comments above each print call expression.
"""
#mystery_string = "Your task is to discover what this string should be."
#mystery_string = "                                                "
#mystery_string = "     k                                           "
#mystery_string = "     k                                           "
#mystery_string = "     k    potential                               "
#mystery_string = "     k    potential                               "
#mystery_string = "     k    potential  regardless                    "
#mystery_string = "U l cki g potential  regardless o   i c m t n e    "
#mystery_string = "Unlocki g potential  regardless o   i c mstance."
mystery_string = "Unlocking potential  regardless of circumstance."

# Should print out 48
print("48 : " +str(len(mystery_string)))

# Should print out 5
print("5 : " +str(mystery_string.index("k")))

# Should print out 4
print("4 : " + str(mystery_string.count("c")))

# Should print out "potential"
print("potential : " + mystery_string[10:19])

# Should print out "sseldrager"
print("sseldrager  :  " + mystery_string[30:20:-1])

# Should print out "Ulcigptnil eadeso icmtne"
print("Ulcigptnil eadeso icmtne  :  " + mystery_string[::2])

# Should print out True
print("True : " + str(mystery_string.startswith("Unlo")))

# Should print out True
print("True : "+ str(mystery_string.endswith("stance.")))

# Should print out 5
print("5 : " + str(len(mystery_string.split())))


