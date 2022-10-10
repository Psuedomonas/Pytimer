# Pytimer
Nicholas Zehm
2-27-21

A simple python timer script. Includes a countdown timer and a stopwatch timer. Console/text based interface.
Requires the vlc player module. 

Edit the following line in the code

playfile = ""

to a real directory for a vlc playable file

movies have not been tested ...
## Changes

Version 1.1.7 (2022-10-9)
* fixed some issues with alarm clock
* file name now in lower case

Version 1.1.6 (2022-4-7)
* Alarm clock now operational!
* Silent countdown and displayed countdown for countdown timer and alarm clock, silent should use less system resources
* Error checking for playfile and alarm_setup method

Version 1.1.5 (2021-3-30)
* Add main menu and stopwatch method. Alarm method not properly implemented yet.
* Add countdownSetup() to allow repeating countdown without needing additional user input
* Fixed bug with Ctrl-C in countdown with undefined p object
* Fixed typos

Version 1.1.2 (2021-3-27)
* Catch bad playfile, put playfile in global scope. Script not complex enough to for this to be an issue.

Version 1.1 (2021-3-12)
* Add hours, deal with negative values (the script worked with negative values, due to the t > 0 check)

## Bugs
* When a decimal place is removed, trailing 0s can appear in output - severity: trivial
* Crash when a bad playfile is used. Try:Exception does not work as the issue is
inside the c coded libvlc library. Workarounds are cumbersome, I will look into this eventually.

### Other Notes
clocks.py is not presently being used. It is intended for the generation of multiple clocks if and when that is implimented.
