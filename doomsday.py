#!/usr/bin/env python

# doomsday.py: a command line trainer for the mental calculation
# of the day of the week for any date in the Gregorian calendar,
# using the Doomsday algorithm original developed by John Horton Conway.

import datetime, calendar, math, random

# Given that the Doomsday algorithm works for the Gregorian calendar,
# we refrain from training on dates earlier than the date of its earliest
# adoption, October 15th, 1582.
OCTOBER_15TH_1582 = datetime.date(1582, 10, 15).toordinal()

# Additionally, we arbitrary limit training to dates no later than 
# the last day of the year 2600.
DECEMBER_31ST_2600 = datetime.date(2600, 12, 31).toordinal()

# From http://stackoverflow.com/questions/739241/python-date-ordinal-output,
# a routine for providing an ordinal description of the day of the date.
def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

# Since datetime.strftime() doesn't handle years earlier than 1900, we provide own date string function.
def date_str(date):
    return "%s %s, %d" % (calendar.month_name[date.month], ordinal(date.day), date.year)

# Returns True if year is a leap year, used in the calculation of doomsmonth().
def leapyear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# The first term in the doomsday.day_of_week() calculation, using
# the formula given in http://en.wikipedia.org/wiki/Doomsday_rule#Finding_a_century.27s_anchor_day.
def doomscentury(date):
    thursday = 4
    c = int(str(date.year)[0:2]) + 1
    return ((((5 * c) + ((c - 1) / 4)) % 7) + thursday) % 7

# The second term in the doomsday.day_of_week() calculation, using
# Fong and Walters' Odds+11 method from http://arxiv.org/abs/1010.0765.
def doomsyear(date):
    x = int(str(date.year)[2:])
    if x % 2 == 1:
        x = x + 11
    x = x / 2
    if x % 2 == 1:
        x = x + 11
    x = x % 7
    return (7 - x) % 7

# The third term in the doomsday.day_of_week() calculation, calculating
# the difference in days between the day of the month in question and
# a Doomsday during the given month.
def doomsmonth(date):
    # In January and February, the doomsday used depends
    # on whether or not the year of the date is a leap year.
    if date.month == 1:
        if leapyear(date.year):
            return date.day - 11
        else:
            return date.day - 10
    elif date.month == 2:
        if leapyear(date.year):
            return date.day - 22
        else:
            return date.day - 21
    # In March we use the 7th as our reference Doomsday.
    elif date.month == 3:
        return date.day - 7
    # Even months after March use the day of the month
    # equal to the month of the year
    elif date.month % 2 == 0:
        return date.day - date.month
    # For the remaining months, we use the "9 to 5 at the 7-11"
    # mnemonic due to Conway
    elif date.month == 5:
        return date.day - 9
    elif date.month == 9:
        return date.day - 5
    elif date.month == 7:
        return date.day - 11
    else: # date.month == 11
        return date.day - 7

# The key equation for the Doomsday algorithm per Fong and Walters in
# http://arxiv.org/abs/1010.0765.
def day_of_week(date):
    return (doomscentury(date) + doomsyear(date) + doomsmonth(date)) % 7

# Verbosely run through the details of the calculation implemented
# by doomsday.day_of_the_week(), for use in training.
def explain_day_of_week(date):
    dc = doomscentury(date)
    dy = doomsyear(date)
    dm = doomsmonth(date)
    dow = day_of_week(date)
    c = int(str(date.year)[0:2]) + 1
    print "%d is in the %s century." % (date.year, ordinal(c))
    print "doomcentury = ((5*%d + floor(%d/4)) mod 7 + Thursday) mod 7" % (c, c-1)
    print "            = ((%d + %d) mod 7 + Thursday) mod 7" % (5*c, (c-1)/4)
    print "            = (%d mod 7 + 4) mod 7" % (5*c+(c-1)/4)
    print "            = (%d + 4) mod 7" % ((5*c+(c-1)/4)%7)
    print "            = %d mod 7" % (((5*c+(c-1)/4) % 7)+4)
    print "            = %d" % dc
    x = int(str(date.year)[2:])
    print "%d is the %s year in the %s century." % (date.year, ordinal(x), ordinal(c))
    print "Let x = %d." % x
    if x % 2 == 1:
        print "%d is odd, so set x = x + 11 = %d" % (x, x + 11)
        x = x + 11
    print "%d / 2 = %d." % (x, x/2)
    x = x / 2
    if x % 2 == 1:
        print "%d is odd, so set x = x + 11 = %d" % (x, x + 11)
        x = x + 11
    print "doomsyear = (7 - (%d mod 7)) mod 7 = (7 - %d) mod 7 = %d mod 7 = %d" % (x, (x%7), (7 - (x%7)), dy)
    if date.month == 1:
        print "%d %s a leap year." % (date.year, "is" if leapyear(date.year) else "is not")
        if leapyear(date.year):
            print "doomsmonth = (%d - 11) = %d" % (date.day, date.day - 11)
        else:
            print "doomsmonth = (%d - 10) = %d" % (date.day, date.day - 10)
    elif date.month == 2:
        print "%d %s a leap year." % (date.year, "is" if leapyear(date.year) else "is not")
        if leapyear(date.year):
            print "doomsmonth = (%d - 22) = %d" % (date.day, date.day - 22)
        else:
            print "doomsmonth = (%d - 21) = %d" % (date.day, date.day - 21)
    elif date.month == 3:
        print "doomsmonth = (%d - 7) = %d" % (date.day, date.day - 7)
        return date.day - 7
    elif date.month % 2 == 0:
        print "doomsmonth = (%d - %d) = %d" % (date.day, date.month, date.day - date.month)
    elif date.month == 5:
        print "doomsmonth = (%d - 9) = %d" % (date.day, date.day - 9)
    elif date.month == 9:
        print "doomsmonth = (%d - 5) = %d" % (date.day, date.day - 5)
    elif date.month == 7:
        print "doomsmonth = (%d - 11) = %d" % (date.day, date.day - 11)
    else: # date.month == 11
        print "doomsmonth = (%d - 7) = %d" % (date.day, date.day - 7)
    print "day of week = (doomscentury + doomsyear + doomsmonth) mod 7 = (%d + %d + %d) mod 7 = %d" % (dc, dy, dm, dow)

# A command line loop for training a user in the mental calculation of
# the day of the week using the Doomsday algorithm.
# The loop prompts user for the day of the week for a random date;
# if the user's answer is incorrect, print out an explanation of the correct calculation.
# The user's accuracy during the session is printed out on exit.
def main():
    trials = 0
    errors = 0
    print "Type 'q' to quit, 0 - 6 for day of week guess."
    while True:
        date = datetime.date.fromordinal(random.randint(OCTOBER_15TH_1582, DECEMBER_31ST_2600))
        input = raw_input("%s? " % date_str(date))
        if input == 'q':
            break
        elif input.isdigit():
            answer = int(input)
            dow = day_of_week(date)
            trials += 1
            if answer == dow:
                print "Correct!"
            else:
                errors += 1
                print "Wrong!"
                explain_day_of_week(date)
        else:
            print "Bad input: type 'q' to quit, 0 - 6 for day of week guess."
    if trials > 0:
        print "Accuracy = %s over %d trial%s" % ("{0:.0f}%".format((1. - ((float(errors) / float(trials)))) * 100), trials, "s" if trials > 1 else "")

if __name__ == '__main__':
    main()
