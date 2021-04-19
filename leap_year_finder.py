# Leap Year Finder in python
# TODO Upgrade this using Tkinter GUI in future

def leap_year():
    """
    This functions seeks to return a leap year after user input << integer(4).
    Rules for a leap year:
    As you surely know, due to some astronomical reasons, years may be leap or common.
    The former are 366 days long, while the latter are 365 days long.

    Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

    -->if the year number isn't divisible by four, it's a common year;
    -->otherwise, if the year number isn't divisible by 100, it's a leap year;
    -->otherwise, if the year number isn't divisible by 400, it's a common year;
    -->otherwise, it's a leap year.

    :return: Year --> Integer
    """

    year = int(input("Enter a year: "))
    mess_1 = 'It\'s a common year!'
    mess_2 = 'It\'s a leap year!'

    if year <= 1582:
        return f'{year} does not fall under Gregorian Calendar!!'
    elif year % 4 != 0:
        return mess_1
    elif year % 100 != 0:
        return mess_2
    elif year % 400 != 0:
        return mess_1
    else:
        return mess_2

print(leap_year())