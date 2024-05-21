#!/usr/bin/python3
# 12-roman_to_int.py


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    my_list= list(map(lambda x : roman_dict[x] , roman_string )) 
    roman_int = sum(my_list)
    return roman_int
