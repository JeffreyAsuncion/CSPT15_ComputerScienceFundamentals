def csSchoolYearsAndGroups(years, groups):
    """
    group_letters = ["a", "b", "c", "d"]
    
    output_list = ""

    for year in range(years):
        for group in range(groups):
            output_list += (str(year+1) + group_letters[group] + ", ")

    return output_list[:-2]
    """

    """
    group_letters = ["a", "b", "c", "d"]
    year_list = ["1", "2", "3", "4", "5", "6", "7"]
    output_list = ""

    for year in range(years):
        for group in range(groups):
            output_list += (year_list[year] + group_letters[group] + ", ")

    result = output_list[:-2]
                                                    
    return result
    """
    condition_years = (years >= 1) and (years <=10)
    condition_groups = (groups >= 1) and ( groups <= 26)
    if  not condition_years or not condition_groups:
        return "Error"
                           
    group_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k",
                    "l","m","n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    output_list = ""

    for year in range(years):
        for group in range(groups):
            output_list += (str(year+1) + group_letters[group] + ", ")

    result = output_list[:-2]
                                                                       
    return result
print(csSchoolYearsAndGroups(years = 7, groups = 4))

    
