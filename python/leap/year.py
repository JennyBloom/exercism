# This Function determines if the tested years in leap_test.py are leap years.

# Notes:
# This exercise was presented poorly in the README and was vague and confusing.
# Originally had it inverted, testing 'if year % 4 == 0' first, but this didn't
# work, I am assuming because of processing-order.

def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    else:
        return True
