# doomsday.py: a Doomsday rule trainer

## Overview
A simple command line utility implemented in Python for practicing mental calculation of the day of the week for dates in the Gregorian calendar, using the Doomsday rule algorithm originally described by John Horton Conway [1]. This implementation relies on recent improvements to the algorithm by Chamberlain Fong and Michael K. Walters [[2]] that reduce the complexity of the mental calculation, as well as on the formula for calculating the anchor day for a century described in the Wikipedia entry for the Doomsday rule [[3]].

## Requirements

Python 2.6 or later.

## Installation

    $ git clone https://github.com/bradleypallen/doomsday.git
    $ cd doomsday
    $ chmod +x *.py
    
## Usage

    $ ./doomsday.py
	Type 'q' to quit, 0 - 6 to enter the day of the week.
	February 8th, 1858? 6
	Wrong! February 8th, 1858 fell on a Monday.
	1) Calculate the anchor day for the 19th century.
	doomcentury = ((5*19 + floor(18/4)) mod 7 + Thursday) mod 7
	            = ((95 + 4) mod 7 + Thursday) mod 7
	            = (99 mod 7 + 4) mod 7
	            = (1 + 4) mod 7
	            = 5 mod 7
	            = 5
	2) Calculate the doomsyear for year 58 in the century.
	doomsyear   = 7's complement of ((58/2)+11 mod 7)
	            = 7's complement of (40 mod 7)
	            = 7's complement of 5
	            = 2
	3) Calculate the doomsmonth for February of the year.
	1858 was not a leap year, so February 21st, 1858 fell on a Doomsday.
	doomsmonth  = 8 - 21
	            = -13
	4) Calculate the day of the week.
	day of week = (doomscentury + doomsyear + doomsmonth) mod 7
	            = (5 + 2 + -13) mod 7
	            = -6 mod 7
	            = 7's complement of (6 mod 7)
	            = 7's complement of 6
	            = 1
	            = Monday
	August 29th, 2129? 1
	Correct! August 29th, 2129 falls on a Monday.
	March 9th, 2580? q
	Accuracy = 50% over 2 trials


## License

This code is provided under the terms of an MIT License [[4]]. See the LICENSE file for the copyright notice.
    
## References

[1] Berlekamp, E.R., Conway, J.H. and Guy, R. K. Winning Ways for your Mathematical Plays. Volume 2: Games In Particular. Academic Press, NY (1982).

[[2]] Fong, C. and Walters, M.K. Methods for Accelerating Conway's Doomsday Algorithm (part 2). ICIAM (2011).

[[3]] Wikipedia. Doomsday rule. Downloaded from http://en.wikipedia.org/wiki/Doomsday_rule (2012).

[[4]] Open Source Initiative (OSI). The MIT License. Downloaded from http://www.opensource.org/licenses/mit-license.php (2012).

[2]: http://arxiv.org/pdf/1010.0765v4.pdf
[3]: http://en.wikipedia.org/wiki/Doomsday_rule
[4]: http://www.opensource.org/licenses/mit-license.php