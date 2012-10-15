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
	October 30th, 2035? 5
	Wrong!
	October 30th, 2035 is in the 21st century.
	doomcentury = ((5*21 + floor(20/4)) mod 7 + Thursday) mod 7
	            = ((105 + 5) mod 7 + Thursday) mod 7
	            = (110 mod 7 + 4) mod 7
	            = (5 + 4) mod 7
	            = 9 mod 7
	            = 2
	2035 is the 35th year in the century.
	doomsyear   = (7 - (((46+11)/2)+11 mod 7)) mod 7
	            = (7 - (34 mod 7)) mod 7
	            = (7 - 6) mod 7
	            = 1 mod 7
	            = 1
	October 10th, 2035 falls on a Doomsday.
	doomsmonth  = 30 - 10
	            = 20
	day of week = (doomscentury + doomsyear + doomsmonth) mod 7
	            = (2 + 1 + 20) mod 7
	            = 23 mod 7
	            = 2
	October 30th, 2035 falls on a Tuesday.
	May 8th, 1905? 1
	Correct!
	May 8th, 1905 fell on a Monday.
	January 21st, 1795? q
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