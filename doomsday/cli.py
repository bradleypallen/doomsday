import click, datetime, calendar, random, readline
from . import methods

# Given that the Doomsday algorithm works for the Gregorian calendar,
# we refrain from training on dates earlier than the date of its earliest
# adoption, October 15th, 1582 (until such time as we manage to capture
# conversion to old/new-style Julian calendars, regional adoption timeframes, etc.)
OCTOBER_15TH_1582 = datetime.date(1582, 10, 15).toordinal()

# Additionally, we arbitrarily limit training to dates no later than
# the last day of the year 2600.
DECEMBER_31ST_2600 = datetime.date(2600, 12, 31).toordinal()

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

# In the explanations of the day of week calculations, we want to use
# the correct tense of the verbs "to fall" and "to be".
def correct_tense(date, past, present, future):
    today = datetime.date.today()
    if date < today:
        return past
    elif date == today:
        return present
    else:
        return future

def explain_leapyear(year):
    if year % 400 == 0:
        print(f'{year} is evenly divisible by 400, so it is a leap year.')
    elif year % 100 == 0:
        print(f'{year} is not evenly divisible by 400, but is evenly divisible by 100, so it is not a leap year.')
    elif year % 4 == 0:
        print(f'{year} is not evenly divisible by neither 400 nor 100, but is evenly divisible by 4, so it is a leap year.')
    else:
        print(f'{year} is not evenly divisible by neither 400, 100, nor 4, so it is not a leap year.')

def explain_doomscentury(year):
    dc = methods.doomscentury(year)
    c = int(str(year)[0:2]) + 1
    print("doomcentury = ((5*%d + floor(%d/4)) mod 7 + Thursday) mod 7" % (c, c-1))
    print("            = ((%d + %d) mod 7 + Thursday) mod 7" % (5*c, (c-1)/4))
    print("            = (%d mod 7 + 4) mod 7" % (5*c+(c-1)/4))
    print("            = (%d + 4) mod 7" % ((5*c+(c-1)/4)%7))
    print("            = %d mod 7" % (((5*c+(c-1)/4) % 7)+4))
    print("            = %d, i.e. %s" % (dc, methods.DAYS_OF_THE_WEEK_NAMES[dc]))

def explain_doomsyear(year):
    dy = methods.doomsyear(year)
    x = int(str(year)[2:])
    x_str = str(x)
    if x % 2 == 1:
        x_str = "(%d+11)" % x
        x = x + 11
    x = x / 2
    x_str = x_str + '/2'
    if x % 2 == 1:
        x_str = "(%s)+11" % x_str
        x = x + 11
    print("doomsyear   = 7's complement of (%s mod 7)" % x_str)
    print("            = 7's complement of (%d mod 7)" % x)
    print("            = 7's complement of %d" % (x%7))
    print("            = %d, i.e. %s" % (dy, methods.DAYS_OF_THE_WEEK_NAMES[dy]))

def explain_doomsmonth(year, month, day):
    dm = methods.doomsmonth(year, month, day)
    date = datetime.date(year, month, day)
    if month == 1:
        print("%d %s%s a leap year, so" % (year, correct_tense(date, "was", "is", "will be"), "" if methods.leapyear(year) else " not")),
        if methods.leapyear(year):
            month_doomsday = 11
        else:
            month_doomsday = 10
    elif month == 2:
        print("%d %s%s a leap year, so" % (year, correct_tense(date, "was", "is", "will be"), "" if methods.leapyear(year) else " not")),
        if methods.leapyear(year):
            month_doomsday = 22
        else:
            month_doomsday = 21
    elif month == 3:
        month_doomsday = 7
    elif month % 2 == 0:
        month_doomsday = month
    elif month == 5:
        month_doomsday = 9
    elif month == 9:
        month_doomsday = 5
    elif month == 7:
        month_doomsday = 11
    else: # month == 11
        month_doomsday = 7
    month_doomsday_date = datetime.date(year, month, month_doomsday)
    print("%s %s on a Doomsday." % (date_str(month_doomsday_date), correct_tense(month_doomsday_date, "fell", "falls", "will fall")))
    print("doomsmonth  = %d - %s" % (day, month_doomsday))
    print("            = %d" % dm)

def explain_day_of_week(year, month, day):
    dc = methods.doomscentury(year)
    dy = methods.doomsyear(year)
    dm = methods.doomsmonth(year, month, day)
    dow = methods.day_of_week(year, month, day)
    print("day of week = (doomscentury + doomsyear + doomsmonth) mod 7")
    print("            = (%d + %d + %d) mod 7" % (dc, dy, dm))
    sum = dc + dy + dm
    print("            = %d mod 7" % sum)
    if sum < 0:
        print("            = 7's complement of (%d mod 7)" % -sum)
        print("            = 7's complement of %d" % (-sum % 7))
        print("            = %d, i.e. %s" % ((-sum % 7), dow))
    else:
        print("            = %d, i.e. %s" % ((sum % 7), dow))

@click.group()
def cli():
    pass

@click.command()
@click.argument('year', type=click.IntRange(1582, 2600))
@click.option('--explain', is_flag=True, help="Provide a walkthrough of the calculation.")
def leapyear(year, explain):
    """Determine if YEAR is a leap year."""
    if explain:
        explain_leapyear(year)
    else:
        click.echo(f'{methods.leapyear(year)}')

@click.command()
@click.argument('year', type=click.IntRange(1582, 2600))
@click.option('--explain', is_flag=True, help="Provide a walkthrough of the calculation.")
def doomscentury(year, explain):
    """Calculate the anchor day for the century of YEAR."""
    if explain:
        explain_doomscentury(year)
    else:
        click.echo(f'{methods.doomscentury(year)}')

@click.command()
@click.argument('year', type=click.IntRange(1582, 2600))
@click.option('--explain', is_flag=True, help="Provide a walkthrough of the calculation.")
def doomsyear(year, explain):
    """Calculate the doomsyear for YEAR."""
    if explain:
        explain_doomsyear(year)
    else:
        click.echo(f'{methods.doomsyear(year)}')

@click.command()
@click.argument('date', type=click.DateTime())
@click.option('--explain', is_flag=True, help="Provide a walkthrough of the calculation.")
def doomsmonth(date, explain):
    """Calculate the doomsmonth for DATE."""
    if explain:
        explain_doomsmonth(date.year, date.month, date.day)
    else:
        click.echo(f'{methods.doomsmonth(date.year, date.month, date.day)}')

@click.command()
@click.argument('date', type=click.DateTime())
@click.option('--explain', is_flag=True, help="Provide a walkthrough of the calculation.")
def dayofweek(date, explain):
    """Calculate the day of the week for DATE."""
    if explain:
        c = int(str(date.year)[0:2]) + 1
        y = int(str(date.year)[2:])
        print("1) Calculate the doomsyear for the %s year of the %s century." % (date_ordinal(y), date_ordinal(c)))
        explain_doomsyear(date.year)
        print("2) Calculate the anchor day for the %s century." % date_ordinal(c))
        explain_doomscentury(date.year)
        print("3) Calculate the doomsmonth for %s of the year." % calendar.month_name[date.month])
        explain_doomsmonth(date.year, date.month, date.day)
        print("4) Calculate the day of the week.")
        explain_day_of_week(date.year, date.month, date.day)
    else:
        click.echo(f'{methods.day_of_week(date.year, date.month, date.day)}')

@click.command()
@click.option('--trials', type=click.IntRange(1, 100), default=10)
def test(trials):
    """Estimate your accuracy in calculating the day of the week."""
    correct_answers = 0
    for i in range(trials):
        date = datetime.date.fromordinal(random.randint(OCTOBER_15TH_1582, DECEMBER_31ST_2600))
        correct_answer = methods.day_of_week(date.year, date.month, date.day)
        answer = input(f'{date_str(date)}? ')
        click.echo(f'{date_str(date)} {correct_tense(date, "was", "is", "will be")} a {correct_answer}.')
        if answer == correct_answer:
            correct_answers += 1
    click.echo(f'Accuracy: {float(correct_answers)/float(trials):.0%} over {trials} trials.')

cli.add_command(leapyear)
cli.add_command(doomscentury)
cli.add_command(doomsyear)
cli.add_command(doomsmonth)
cli.add_command(dayofweek)
cli.add_command(test)

if __name__ == '__main__':
    cli()
