# doomsday.py: a Doomsday rule trainer

## Overview
A simple command line utility implemented in Python for practicing mental calculation of the day of the week for dates in the Gregorian calendar, using the Doomsday rule algorithm originally described by John Horton Conway [1]. This implementation relies on recent improvements to the algorithm by Chamberlain Fong and Michael K. Walters [[2]] that reduce the complexity of the mental calculation as well as the formula for calculating the anchor day for a century described in the Wikipedia entry for the Doomsday rule [[3]].

## Requirements

Python 2.6 or later.

## Installation

    $ git clone https://github.com/bradleypallen/doomsday.git
    $ cd doomsday
    $ chmod +x *.py
    
## Usage

    $ ./doomsday.py
    Type 'q' to quit, 0 - 6 for day of week guess.
	December 9th, 1917? 3
	Wrong!
	1917 is in the 20 century.
	doomcentury = ((5*20 + floor(19/4)) mod 7 + Thursday) mod 7
	            = ((100 + 4) mod 7 + Thursday) mod 7
	            = (104 mod 7 + 4) mod 7
	            = (6 + 4) mod 7
	            = 10 mod 7
	            = 3
	1917 is the 17th year in the 20th century.
	Let x = 17.
	17 is odd, so set x = x + 11 = 28
	28 / 2 = 14.
	doomsyear = (7 - (14 mod 7)) mod 7 = (7 - 0) mod 7 = 7 mod 7 = 0
	doomsmonth = (9 - 12) = -3
	day of week = (doomscentury + doomsyear + doomsmonth) mod 7 = (3 + 0 + -3) mod 7 = 0
	April 9th, 2000? 0
	Correct!
	May 26th, 1679? q
	Accuracy = 50% over 2 trials
	$


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