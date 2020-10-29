def csOppositeReverse(txt):
    """
    txt = txt[::-1]     
    new_string = ""
    for i in txt:
        if i == " ":
            new_string += i
        if i.isupper():
            new_string += i.lower()
            continue
        if i.islower():
            new_string += i.upper()
            continue
        else:
            pass
    
    return new_string
    """
        
    txt = txt[::-1]
    new_string = ""
    for i in txt:
        if i == " ":
            new_string += i
        elif i.isupper():
            new_string += i.lower()
            continue
        else: #i.islower():
            new_string += i.upper()

    return new_string

print(csOppositeReverse("Hello World"))
print(csOppositeReverse("ReVeRsE"))
print(csOppositeReverse("Radar"))
