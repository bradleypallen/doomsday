#!/usr/bin/env python

import datetime, calendar, math, random

# doomsday.py: a command line trainer for the mental calculation
# of the day of the week for any date in the Gregorian calendar,
# using the Doomsday algorithm original developed by John Horton Conway.

# Given that the Doomsday algorithm works for the Gregorian calendar,
# we refrain from training on dates earlier than the date of its earliest
# adoption, October 15th, 1582 (until such time as we manage to capture
# conversion to old/new-style Julian calendars, regional adoption timeframes, etc.)
OCTOBER_15TH_1582 = datetime.date(1582, 10, 15).toordinal()

# Additionally, we arbitrarily limit training to dates no later than 
# the last day of the year 2600.
DECEMBER_31ST_2600 = datetime.date(2600, 12, 31).toordinal()

# We store the strings for the names of the days of the week so that we can map
# the computed day of the week to its name.
dow_name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# From http://stackoverflow.com/questions/739241/python-date-ordinal-output,
# we include a routine for providing an ordinal description of the day of the date.
def date_ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
        return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

# Since datetime.strftime() doesn't handle years earlier than 1900, we provide own date string function.
def date_str(date):
    return "%s %s, %d" % (calendar.month_name[date.month], date_ordinal(date.day), date.year)

# In the explanation of the day of week calculation, we want to use
# the correct tense of the verbs "to fall" and "to be".
def correct_tense(date, past, present_or_future):
    return past if date < datetime.date.today() else present_or_future

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
    # Explain the calculation of the doomscentury term.
    dc = doomscentury(date)
    c = int(str(date.year)[0:2]) + 1
    print "1) Calculate the anchor day for the %s century." % date_ordinal(c)
    print "doomcentury = ((5*%d + floor(%d/4)) mod 7 + Thursday) mod 7" % (c, c-1)
    print "            = ((%d + %d) mod 7 + Thursday) mod 7" % (5*c, (c-1)/4)
    print "            = (%d mod 7 + 4) mod 7" % (5*c+(c-1)/4)
    print "            = (%d + 4) mod 7" % ((5*c+(c-1)/4)%7)
    print "            = %d mod 7" % (((5*c+(c-1)/4) % 7)+4)
    print "            = %d" % dc
    # Explain the calculation of the doomsyear term.
    dy = doomsyear(date)
    x = int(str(date.year)[2:])
    print "2) Calculate the doomsyear for year %s in the century." % x
    x_str = str(x)
    if x % 2 == 1:
        x_str = "(%d+11)" % x
        x = x + 11
    x = x / 2
    x_str = x_str + '/2'
    if x % 2 == 1:
        x_str = "(%s)+11" % x_str
        x = x + 11
    print "doomsyear   = 7's complement of (%s mod 7)" % x_str
    print "            = 7's complement of (%d mod 7)" % x
    print "            = 7's complement of %d" % (x%7)
    print "            = %d" % dy
    # Explain the calculation of the doomsmonth term.
    dm = doomsmonth(date)
    print "3) Calculate the doomsmonth for %s of the year." % calendar.month_name[date.month]
    if date.month == 1:
        print "%d %s%s a leap year, so" % (date.year, correct_tense(date, "was", "is"), "" if leapyear(date.year) else " not"),
        if leapyear(date.year):
            month_doomsday = 11
        else:
            month_doomsday = 10
    elif date.month == 2:
        print "%d %s%s a leap year, so" % (date.year, correct_tense(date, "was", "is"), "" if leapyear(date.year) else " not"), 
        if leapyear(date.year):
            month_doomsday = 22
        else:
            month_doomsday = 21
    elif date.month == 3:
        month_doomsday = 7
    elif date.month % 2 == 0:
        month_doomsday = date.month
    elif date.month == 5:
        month_doomsday = 9
    elif date.month == 9:
        month_doomsday = 5
    elif date.month == 7:
        month_doomsday = 11
    else: # date.month == 11
        month_doomsday = 7
    month_doomsday_date = datetime.date(date.year, date.month, month_doomsday)
    print "%s %s on a Doomsday." % (date_str(month_doomsday_date), correct_tense(month_doomsday_date, "fell", "falls"))
    print "doomsmonth  = %d - %s" % (date.day, month_doomsday)
    print "            = %d" % dm
    # Finally, explain the day of week calculation.
    dow = day_of_week(date)
    print "4) Calculate the day of the week."
    print "day of week = (doomscentury + doomsyear + doomsmonth) mod 7"
    print "            = (%d + %d + %d) mod 7" % (dc, dy, dm)
    sum = dc + dy + dm
    print "            = %d mod 7" % sum
    if sum < 0:
        print "            = 7's complement of (%d mod 7)" % -sum
        print "            = 7's complement of %d" % (-sum % 7)
    print "            = %d" % dow
    print "            = %s" % dow_name[dow]

# A command line loop for training a user in the mental calculation of
# the day of the week using the Doomsday algorithm.
# The loop prompts user for the day of the week for a random date;
# if the user's answer is incorrect, print out an explanation of the correct calculation.
# The user's accuracy during the session is printed out on exit.
def main():
    trials = 0
    errors = 0
    print "Type 'q' to quit, 0 - 6 to enter the day of the week."
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
                print "Correct! %s %s on a %s." % (date_str(date), correct_tense(date, "fell", "falls"), dow_name[dow])

            else:
                errors += 1
                print "Wrong! %s %s on a %s." % (date_str(date), correct_tense(date, "fell", "falls"), dow_name[dow])
                explain_day_of_week(date)
        else:
            print "Bad input: type 'q' to quit, 0 - 6 to enter the day of the week."
    if trials > 0:
        print "Accuracy = %s over %d trial%s" % ("{0:.0f}%".format((1. - ((float(errors) / float(trials)))) * 100), trials, "s" if trials > 1 else "")

if __name__ == '__main__':
    main()
