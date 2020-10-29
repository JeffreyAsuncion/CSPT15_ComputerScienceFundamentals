def csAlphanumericRestriction(input_str):
    if input_str == "" or " " in input_str:
        return False
                    
    if input_str[0].isalpha():
        for i in range(len(input_str)):
            if input_str[i].isalpha() == False:
                return False
        return True
                                                                           
    elif input_str[0].isnumeric():
        for i in range(len(input_str)):
            if input_str[i].isnumeric() == False:
                return False
        return True
                                                                                                                                
    else:
        return False  

print(csAlphanumericRestriction("Bold")) # True
print(csAlphanumericRestriction("123454321")) # True
print(csAlphanumericRestriction("H3LL0")) # False

