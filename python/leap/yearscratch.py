# This is a scratch file of all my work prior to final year.py
# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

# The leap_test.py program expects module named year containing the function 'is_leap_year()'
# #2 tests failed:
# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 == 0:
#             #print("The year, " + str(year) + ", is a leap year.")
#             return True
#         # else:
#         #     #print("The year, " + str(year) + ", is not a leap year.")
#         #     return False
#     elif year % 4 != 0:
#         return False

#One test Failed
# def is_leap_year(year):
#     if year % 4 == 0:
#         return True
#     elif year % 4 == 0 and year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0:
#         return False
#     else:
#         return False

# #One fail
# def is_leap_year(year):
#     if year % 4 == 0 and year % 100 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0 and year % 400:
#         return True
#     else:
#         return False

# # #One fail
# def is_leap_year(year):
#     if year % 4 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0:
#         return False
#     elif year % 4 == 0 or year % 100 == 0 and year % 400:
#         return True
#     else:
#         return False

#One fail
# def is_leap_year(year):
#     if year % 4 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 400 == 0:
#         return True
#     elif year % 100 == 0 and year % 400 == 0:
#         return False
#     else:
#         return False

# One fail
# def is_leap_year(year):
#     if year % 4 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0:
#         return False
#     elif year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return False

#THis is the one:
# def is_leap_year(year):
#     if year % 4 != 0:
#         return False
#     elif year % 4 == 0 and year % 400 == 0:
#         return True
#     elif year % 4 == 0 and year % 100 == 0:
#         return False
#     else:
#         return True
