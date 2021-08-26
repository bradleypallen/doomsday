# doomsday: a Doomsday rule utility and trainer
[![PyPI](https://img.shields.io/pypi/v/doomsday.svg)](https://pypi.org/project/doomsday/)
[![Changelog](https://img.shields.io/github/v/release/bradleypallen/doomsday?include_prereleases&label=changelog)](https://github.com/bradleypallen/doomsday/releases)
[![Tests](https://github.com/bradleypallen/doomsday/workflows/Test/badge.svg)](https://github.com/bradleypallen/doomsday/actions?query=workflow%3ATest)
[![License](https://img.shields.io/github/license/bradleypallen/doomsday)](https://github.com/bradleypallen/doomsday/blob/main/LICENSE)

A simple command line utility implemented in Python for practicing mental calculation of the day of the week for dates in the Gregorian calendar, using the Doomsday rule algorithm originally described by John Horton Conway [1]. This implementation relies on recent improvements to the algorithm by Chamberlain Fong and Michael K. Walters [[2]] that reduce the complexity of the mental calculation, as well as on the formula for calculating the anchor day for a century described in the Wikipedia entry for the Doomsday rule [[3]].

```
$ doomsday --help
Usage: doomsday [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dayofweek     Calculate the day of the week for DATE.
  doomscentury  Calculate the anchor day for the century of YEAR.
  doomsmonth    Calculate the doomsmonth for DATE.
  doomsyear     Calculate the doomsyear for YEAR.
  leapyear      Determine if YEAR is a leap year.
  test          Estimate your accuracy in calculating the day of the week.

$ doomsday leapyear --help
Usage: doomsday leapyear [OPTIONS] YEAR

  Determine if YEAR is a leap year.

Options:
  --explain  Provide a walkthrough of the calculation.
  --help     Show this message and exit.

$ doomsday doomscentury --help
Usage: doomsday doomscentury [OPTIONS] YEAR

  Calculate the anchor day for the century of YEAR.

Options:
  --explain  Provide a walkthrough of the calculation.
  --help     Show this message and exit.

$ doomsday doomsyear --help
Usage: doomsday doomsyear [OPTIONS] YEAR

  Calculate the doomsyear for YEAR.

Options:
  --explain  Provide a walkthrough of the calculation.
  --help     Show this message and exit.

$ doomsday doomsmonth --help
Usage: doomsday doomsmonth [OPTIONS] [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d
                           %H:%M:%S]

  Calculate the doomsmonth for DATE.

Options:
  --explain  Provide a walkthrough of the calculation.
  --help     Show this message and exit.

$ doomsday dayofweek --help
Usage: doomsday dayofweek [OPTIONS] [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d
                          %H:%M:%S]

  Calculate the day of the week for DATE.

Options:
  --explain  Provide a walkthrough of the calculation.
  --help     Show this message and exit.

$ doomsday test --help
Usage: doomsday test [OPTIONS]

  Estimate your accuracy in calculating the day of the week.

Options:
  --trials INTEGER RANGE  [1<=x<=100]
  --help                  Show this message and exit.
```

## Requirements

Python 3.6 or later.

## Installation

    $ pip install doomsday

## License

This code is provided under the terms of an MIT License. See the LICENSE file for the copyright notice.

## References

[1] Berlekamp, E.R., Conway, J.H. and Guy, R. K. Winning Ways for your Mathematical Plays. Volume 2: Games In Particular. Academic Press, NY (1982).

[[2]] Fong, C. and Walters, M.K. Methods for Accelerating Conway's Doomsday Algorithm (part 2). ICIAM (2011).

[[3]] Wikipedia. Doomsday rule. Downloaded from http://en.wikipedia.org/wiki/Doomsday_rule (2012).

[2]: http://arxiv.org/pdf/1010.0765v4.pdf
[3]: http://en.wikipedia.org/wiki/Doomsday_rule
