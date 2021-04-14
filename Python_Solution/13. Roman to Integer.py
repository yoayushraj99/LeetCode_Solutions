# Easy

def romanToInt(self, s: str) -> int:
    roman_value = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    int_value = roman_value[s[-1]]

    for i in range(len(s) - 1):
        if roman_value[s[i]] < roman_value[s[i + 1]]:
            int_value -= roman_value[s[i]]
        else:
            value = roman_value[s[i]]
            int_value += value
    return int_value

