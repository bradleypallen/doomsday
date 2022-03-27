import click
from click.testing import CliRunner
from doomsday import cli

DAYOFWEEK_TEST_OUTPUT_1 = """1) Calculate the doomsyear for the 22nd year of the 21st century.
doomsyear   = 7's complement of ((22/2)+11 mod 7)
            = 7's complement of (22 mod 7)
            = 7's complement of 1
            = 6, i.e. Saturday
2) Calculate the anchor day for the 21st century.
doomcentury = ((5*21 + floor(20/4)) mod 7 + Thursday) mod 7
            = ((105 + 5) mod 7 + Thursday) mod 7
            = (110 mod 7 + 4) mod 7
            = (5 + 4) mod 7
            = 9 mod 7
            = 2, i.e. Tuesday
3) Calculate the doomsmonth for March of the year.
March 7th, 2022 fell on a Doomsday.
doomsmonth  = 26 - 7
            = 19
4) Calculate the day of the week.
day of week = (doomscentury + doomsyear + doomsmonth) mod 7
            = (2 + 6 + 19) mod 7
            = 27 mod 7
            = 6, i.e. Saturday
"""

DAYOFWEEK_TEST_OUTPUT_2 = """1) Calculate the doomsyear for the 21st year of the 21st century.
doomsyear   = 7's complement of ((21+11)/2 mod 7)
            = 7's complement of (16 mod 7)
            = 7's complement of 2
            = 5, i.e. Friday
2) Calculate the anchor day for the 21st century.
doomcentury = ((5*21 + floor(20/4)) mod 7 + Thursday) mod 7
            = ((105 + 5) mod 7 + Thursday) mod 7
            = (110 mod 7 + 4) mod 7
            = (5 + 4) mod 7
            = 9 mod 7
            = 2, i.e. Tuesday
3) Calculate the doomsmonth for January of the year.
2021 was not a leap year, so
January 10th, 2021 fell on a Doomsday.
doomsmonth  = 15 - 10
            = 5
4) Calculate the day of the week.
day of week = (doomscentury + doomsyear + doomsmonth) mod 7
            = (2 + 5 + 5) mod 7
            = 12 mod 7
            = 5, i.e. Friday
"""

DAYOFWEEK_TEST_OUTPUT_3 = """1) Calculate the doomsyear for the 58th year of the 20th century.
doomsyear   = 7's complement of ((58/2)+11 mod 7)
            = 7's complement of (40 mod 7)
            = 7's complement of 5
            = 2, i.e. Tuesday
2) Calculate the anchor day for the 20th century.
doomcentury = ((5*20 + floor(19/4)) mod 7 + Thursday) mod 7
            = ((100 + 4) mod 7 + Thursday) mod 7
            = (104 mod 7 + 4) mod 7
            = (6 + 4) mod 7
            = 10 mod 7
            = 3, i.e. Wednesday
3) Calculate the doomsmonth for November of the year.
November 7th, 1958 fell on a Doomsday.
doomsmonth  = 26 - 7
            = 19
4) Calculate the day of the week.
day of week = (doomscentury + doomsyear + doomsmonth) mod 7
            = (3 + 2 + 19) mod 7
            = 24 mod 7
            = 3, i.e. Wednesday
"""

def test_dayofweek():
    runner = CliRunner()
    result = runner.invoke(cli.dayofweek, ['2022-03-26', '--explain'])
    assert result.exit_code == 0
    assert result.output == DAYOFWEEK_TEST_OUTPUT_1
    result = runner.invoke(cli.dayofweek, ['2021-01-15', '--explain'])
    assert result.exit_code == 0
    assert result.output == DAYOFWEEK_TEST_OUTPUT_2
    result = runner.invoke(cli.dayofweek, ['1958-11-26', '--explain'])
    assert result.exit_code == 0
    assert result.output == DAYOFWEEK_TEST_OUTPUT_3

DOOMSCENTURY_TEST_OUTPUT_1 = """doomcentury = ((5*23 + floor(22/4)) mod 7 + Thursday) mod 7
            = ((115 + 5) mod 7 + Thursday) mod 7
            = (120 mod 7 + 4) mod 7
            = (1 + 4) mod 7
            = 5 mod 7
            = 5, i.e. Friday
"""

DOOMSCENTURY_TEST_OUTPUT_2 = """doomcentury = ((5*20 + floor(19/4)) mod 7 + Thursday) mod 7
            = ((100 + 4) mod 7 + Thursday) mod 7
            = (104 mod 7 + 4) mod 7
            = (6 + 4) mod 7
            = 10 mod 7
            = 3, i.e. Wednesday
"""

def test_doomscentury():
    runner = CliRunner()
    result = runner.invoke(cli.doomscentury, ['2201', '--explain'])
    assert result.exit_code == 0
    assert result.output == DOOMSCENTURY_TEST_OUTPUT_1
    result = runner.invoke(cli.doomscentury, ['1903', '--explain'])
    assert result.exit_code == 0
    assert result.output == DOOMSCENTURY_TEST_OUTPUT_2

DOOMSMONTH_TEST_OUTPUT_1 = """March 7th, 2022 fell on a Doomsday.
doomsmonth  = 26 - 7
            = 19
"""

DOOMSMONTH_TEST_OUTPUT_2 = """2021 was not a leap year, so
January 10th, 2021 fell on a Doomsday.
doomsmonth  = 15 - 10
            = 5
"""

def test_doomsmonth():
    runner = CliRunner()
    result = runner.invoke(cli.doomsmonth, ['2022-03-26', '--explain'])
    assert result.exit_code == 0
    assert result.output == DOOMSMONTH_TEST_OUTPUT_1
    result = runner.invoke(cli.doomsmonth, ['2021-01-15', '--explain'])
    assert result.exit_code == 0
    assert result.output == DOOMSMONTH_TEST_OUTPUT_2

DOOMSYEAR_TEST_OUTPUT_1 = """doomsyear   = 7's complement of ((22/2)+11 mod 7)
            = 7's complement of (22 mod 7)
            = 7's complement of 1
            = 6, i.e. Saturday
"""

DOOMSYEAR_TEST_OUTPUT_2 = """doomsyear   = 7's complement of (((3+11)/2)+11 mod 7)
            = 7's complement of (18 mod 7)
            = 7's complement of 4
            = 3, i.e. Wednesday
"""

def test_doomsyear():
    runner = CliRunner()
    result = runner.invoke(cli.doomsyear, ['2022', '--explain'])
    assert result.exit_code == 0
    assert result.output == DOOMSYEAR_TEST_OUTPUT_1
    result = runner.invoke(cli.doomsyear, ['1903', '--explain'])
    assert result.exit_code == 0
    assert result.output == DOOMSYEAR_TEST_OUTPUT_2

LEAPYEAR_TEST_OUTPUT_1 = """1903 is not evenly divisible by neither 400, 100, nor 4, so it is not a leap year.
"""

LEAPYEAR_TEST_OUTPUT_2 = """2024 is not evenly divisible by neither 400 nor 100, but is evenly divisible by 4, so it is a leap year.
"""

LEAPYEAR_TEST_OUTPUT_3 = """1900 is not evenly divisible by 400, but is evenly divisible by 100, so it is not a leap year.
"""

def test_leapyear():
    runner = CliRunner()
    result = runner.invoke(cli.leapyear, ['1903', '--explain'])
    assert result.exit_code == 0
    assert result.output == LEAPYEAR_TEST_OUTPUT_1
    result = runner.invoke(cli.leapyear, ['2024', '--explain'])
    assert result.exit_code == 0
    assert result.output == LEAPYEAR_TEST_OUTPUT_2
    result = runner.invoke(cli.leapyear, ['1900', '--explain'])
    assert result.exit_code == 0
    assert result.output == LEAPYEAR_TEST_OUTPUT_3
