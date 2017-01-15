# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def deter_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    if year1 == year2:
        month = month1
        while month < month2:
            if deter_leap_year(year1) and month == 2:
                total = total + 29
            else:
                total = total + daysOfMonths[month-1]
            month = month + 1
        return total - day1 + day2
    else:
        year = year1 + 1
        month = month1
        while month <= 12:
            if deter_leap_year(year1) and month == 2:
                total = total + 29
            else:
                total = total + daysOfMonths[month-1]
            month = month + 1
        total = total - day1
        month = 1
        while month < month2:
            if deter_leap_year(year2) and month == 2:
                total = total + 29
            else:
                total = total + daysOfMonths[month-1]
            month = month + 1
        total = total + day2
        while year < year2:
            if deter_leap_year(year):
                total = total + 366
            else:
                total = total + 365
            year = year + 1
        return total


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()