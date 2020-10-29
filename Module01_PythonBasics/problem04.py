def csSquareAllDigits(n):
    
    string_n = str(n)
    output_str = ""
    
    for i in string_n:
        s2 = (int(i))**2
        output_str += str(s2)

    return int(output_str)










print(csSquareAllDigits(9119)) # 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
print(csSquareAllDigits(2483))
