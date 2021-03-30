#!/usr/bin/python3.8
# Filename: Pytimer.py
'''
Nicholas Zehm
Pytimer.py
2021-2-27

A simple python timer script. Console/text based interface. Requires the vlc player module.
Version 1.1.5
'''

#### EDIT THIS: provide a valid file (vlc usable) for playfile. This will be used as default/fallback ####
playfile = ""


#import modules
import time
import os   #for path to music/sound
import vlc  #this module is from the vlc team, and is required for music/sound


#
#  name: stopwatch
#  @param none
#  @return main()
#
def stopwatch():
    t = 0
    h = 0
    mins = 0
    secs = 0
    print('Type Ctrl-C to stop timer')
    print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')
    #Ctrl-C causes KeyboardInterrupt to be raised
    try:
        while True:
            t += 1
            time.sleep(1)
            h, m = divmod(t, 3600)
            mins, secs = divmod(m, 60)
            print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')


    except KeyboardInterrupt:
        pass

    print('\nStop Time')
    print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')
    input("\nPress 'Enter' to return to main menu...")
    return main()


#
#  name: countdownSetup
#  @param playfile
#  @return countdown(playfile, T)
#
def countdownSetup(playfile):
    try:
        h = int(input("hours: "))
    except:
        print("0 hours")
        h = 0
    if h < 0:
        h = 0
        print("0 hours")

    try:
        m = int(input("minutes: "))
    except:
        print("0 minutes")
        m=0
    if m < 0:
        m = 0
        print("0 minutes")

    try:
        s = int(input("seconds: "))
    except:
        s=0
        print("0 seconds")
    if s < 0:
        s = 0
        print("0 seconds")

    a = input("User defined alarm sound? y/n: ")

    if a == 'y':
        path = input("Input sound file directory (no ""s): ")

        isFile = os.path.isfile(path)
        if isFile == True:
            playfile = path
            print("Using {0}".format(playfile))
        else:
            print("Error: Using default sound.")

    T = h * 60 * 60 + m * 60 + s

    return countdown(playfile, T)


#
#  name: countdown
#  @param playfile, T
#  @return main() or countdown
#
def countdown(playfile, T):
    t = T
    #Ctrl-C causes KeyboardInterrupt to be raised
    try:
        while True and t > 0:
            h, m = divmod(t, 3600)
            mins, secs = divmod(m, 60)
            print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')
            time.sleep(1)
            t -= 1
        p = vlc.MediaPlayer(playfile)
        p.play()
        input("Sounding the alarm...")
    except KeyboardInterrupt:
        return main()

    p.stop()

    r = input("Repeat countdown? (y/n): ")
    if r == 'y':
        return countdown(playfile, T)
    else:
        return main()


#
#  name: alarm
#  @param sound object
#  @return main()
#
def alarm(playfile):
    print('Alarm not implemented yet')
    '''
    r = input("repeat alarm? (y/n): ")
    if r == 'y':
        pass
    else:
        pass
    d = input("day(s) (format MTWThFStSn): ")
    #parse d for chars
    #set day(s) for alarm

    day = 'M'
    alarm_day = 'M'
    t = input("time (format use military time, h:m): ")

    if day == alarm_day:
        #set an alarm for day at specified time
    '''

    return main()


#
#  name: main
#  @param none
#  @return  function
#
def main():
    choice = input("Press 'a' for alarm, 'c' for countdown timer, 's' for stopwatch, or 'x' to exit: ")

    if choice == 'a':
        return alarm(playfile)
    elif choice == 'c':
        return countdownSetup(playfile)
    elif choice == 's':
        return stopwatch()
    elif choice == 'x':
        exit()
    else:
        main()


main()
