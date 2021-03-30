# Pytimer
Nicholas Zehm
2-27-21

A simple python timer script. Console/text based interface.
Requires the vlc player module.

Edit the following line in the code

playfile = ""

to a real directory for a vlc playable file

movies have not been tested ...
# Changes
Version 1.1 (2021-3-12)
* Add hours, deal with negative values (the script worked with negative values, due to the t > 0 check)

Version 1.1.2 (2021-3-27)
* Catch bad playfile, put playfile in global scope. Script not complex enough to for this to be an issue.

Version 1.1.5 (2021-3-30)
* Add main menu and stopwatch method. Alarm method not properly implemented yet.
* Add countdownSetup() to allow repeating countdown without needing additional user input
* Fixed bug with Ctrl-C in countdown with undefined p object
* Fixed typos

# Bugs
* sometimes there is a trailing 0 in the output, caused by decimal place drop in h, mins, or secs - severity: trivial
* Alarm not implemented
