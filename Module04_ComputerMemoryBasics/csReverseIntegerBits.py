"""
Given an integer, write a function that reverses the bits (in binary) and returns the integer result.

Examples:

csReverseIntegerBits(417) -> 267
417 in binary is 110100001. Reversing the binary is 100001011, which is 267 in decimal.
csReverseIntegerBits(267) -> 417
csReverseIntegerBits(0) -> 0

"""

def csReverseIntegerBits(n):

    # https://www.geeksforgeeks.org/reverse-actual-bits-given-number/
    rev = 0
      
    # traversing bits of 'n' from the right 
    while (n > 0) : 
          
        # bitwise left shift 'rev' by 1 
        rev = rev << 1
          
        # if current bit is '1' 
        if (n & 1 == 1) : 
            rev = rev ^ 1
          
        # bitwise right shift 'n' by 1 
        n = n >> 1
          
      
    # required number 
    return rev 


print(csReverseIntegerBits(267))# -> 417
print(csReverseIntegerBits(0))# -> 0
