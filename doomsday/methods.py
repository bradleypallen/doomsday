# We store the strings for the names of the days of the week so that we can map
# the computed day of the week to its name.
DAYS_OF_THE_WEEK_NAMES = [ 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ]

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
def doomscentury(year):
    thursday = 4
    c = int(str(year)[0:2]) + 1
    return int((((5 * c) + ((c - 1) / 4)) % 7) + thursday) % 7

# The second term in the doomsday.day_of_week() calculation, using
# Fong and Walters' Odds+11 method from http://arxiv.org/abs/1010.0765.
def doomsyear(year):
    x = int(str(year)[2:])
    if x % 2 == 1:
        x = x + 11
    x = x / 2
    if x % 2 == 1:
        x = x + 11
    x = x % 7
    return int((7 - x) % 7)

# The third term in the doomsday.day_of_week() calculation, calculating
# the difference in days between the day of the month in question and
# a Doomsday during the given month.
def doomsmonth(year, month, day):
    # In January and February, the doomsday used depends
    # on whether or not the year of the date is a leap year.
    if month == 1:
        if leapyear(year):
            return day - 11
        else:
            return day - 10
    elif month == 2:
        if leapyear(year):
            return day - 22
        else:
            return day - 21
    # In March we use the 7th as our reference Doomsday.
    elif month == 3:
        return day - 7
    # Even months after March use the day of the month
    # equal to the month of the year
    elif month % 2 == 0:
        return day - month
    # For the remaining months, we use the "9 to 5 at the 7-11"
    # mnemonic due to Conway
    elif month == 5:
        return day - 9
    elif month == 9:
        return day - 5
    elif month == 7:
        return day - 11
    else: # month == 11
        return day - 7

# The key equation for the Doomsday algorithm per Fong and Walters in
# http://arxiv.org/abs/1010.0765.
def day_of_week(year, month, day, name=True):
    dow = (doomscentury(year) + doomsyear(year) + doomsmonth(year, month, day)) % 7
    if name:
        return DAYS_OF_THE_WEEK_NAMES[dow]
    else:
        return dow
