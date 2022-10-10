#!/usr/bin/python3.10
# Filename: Pytimer.py
'''
Nicholas Zehm
Pytimer.py
2021-2-27
A simple python timer script. Console/text based interface. Requires the vlc player module.
Version 1.1.7 2022-10-9
'''

#### EDIT THIS: provide a valid file (vlc usable) for playfile. This will be used as default/fallback ####
playfile = ""


#import modules
import time
import os   #for path to music/sound
import vlc  #this module is from the vlc team, and is required for music/sound
import datetime  #for alarm clock


#
#  name: stopwatch
#  @param none
#  @return main()
#
def stopwatch():
    try:
        t = 0
        h = 0
        mins = 0
        secs = 0
        print('Type Ctrl-C to stop timer')
        print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')

        while True:
            t += 1
            time.sleep(1)
            h, m = divmod(t, 3600)
            mins, secs = divmod(m, 60)
            print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')

        print('\nStop Time')
        print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')
        input("\nPress 'Enter' to return to main menu...")
        return main()

    except KeyboardInterrupt:
        return main()


#
#  name: countdownSetup
#  @param playfile
#  @return countdown(playfile, T)
#
def countdown_setup(playfile, playfile_exists):
    try:
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

        if not playfile_exists:
            print("NOTE: No default sound selected")

        a = input("User defined alarm sound? (y/n): ")

        if a == 'y':
            path = input("Input sound file directory (no ""s): ")

            isFile = os.path.isfile(path)
            if isFile == True:
                playfile = path
                print("Using {0}".format(playfile))
                playfile_exists == True
            elif playfile_exists == True:
                print("Error: Using default sound.")
            else:
                print("Warning! No sound file. Alarm will be silent.")

        if not playfile_exists:
            print("Warning! No sound file. Alarm will be silent.")

        T = h * 60 * 60 + m * 60 + s

        show_counter = input("Countdown output until alarm? (y/n): ")

        if show_counter == 'n':
            return silent_countdown(playfile, playfile_exists, T)
        else:
            return countdown(playfile, playfile_exists, T)

    except KeyboardInterrupt:
        return main()

#
#  name: countdown
#  @param playfile, T
#  @return main() or countdown
#
def countdown(playfile, playfile_exists, T):
    try:
        t = T

        while True and t > 0:
            h, m = divmod(t, 3600)
            mins, secs = divmod(m, 60)
            print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')
            time.sleep(1)
            t -= 1
        if playfile_exists:
            p = vlc.MediaPlayer(playfile)
            p.play()
        else:
            print("SILENT ALARM!")
        input("Sounding the alarm...")

        if playfile_exists:
            p.stop()

        r = input("Repeat countdown? (y/n): ")
        if r == 'y':
            return countdown(playfile, playfile_exists, T)
        else:
            return main()

    except KeyboardInterrupt:
        return main()

#
#   name: silent_countdown
#   @param playfile, T
#   @return main() or silent_countdown
#
def silent_countdown(playfile, playfile_exists, T):
    try:
        t = T
        time.sleep(t)

        if playfile_exists:
            p = vlc.MediaPlayer(playfile)
            p.play()
        else:
            print("SILENT ALARM!")

        input("Sounding the alarm...")

        if playfile_exists:
            p.stop()

        r = input("Repeat countdown? (y/n): ")
        if r == 'y':
            return silent_countdown(playfile, playfile_exists, T)
        else:
            return main()

    except KeyboardInterrupt:
        return main()


#
#   name: alarm_setup
#   @param sound object
#   @return alarm()
#
def alarm_setup(playfile, playfile_exists):
    try:    # Ctrl C to return to main menu

        try:    # bad values will reset the function
            print("Set the alarm time")
            hour = int(input('Hour (0-23) '))
            if hour < 0:
                print('no negative numbers')
                return alarm_setup(playfile, playfile_exists)
        except:
            print('bad value')
            return alarm_setup(playfile, playfile_exists)

        try:    # bad values will reset the function
            minute = int(input('Minute (0-59): '))
            if minute < 0:
                print('no negative numbers')
                return alarm_setup(playfile, playfile_exists)
            elif minute > 59:
                print('Must be less than 59 minutes')
                return alarm_setup(playfile, playfile_exists)
        except:
            print('bad value')
            return alarm_setup(playfile, playfile_exists)

        if not playfile_exists:
            print("NOTE: No default sound selected")

        a = input("User defined alarm sound? (y/n): ")
        if a == 'y':
            path = input("Input sound file directory (no ""s): ")

            isFile = os.path.isfile(path)
            if isFile == True:
                playfile = path
                print("Using {0}".format(playfile))
                playfile_exists == True

            elif playfile_exists == True:
                print("Error: Using default sound.")

            else:
                print("Warning! No sound file. Alarm will be silent.")

        if not playfile_exists:
            print("Warning! No sound file. Alarm will be silent.")

        show_counter = input("Show countdown timer to alarm? (y/n): ")

        if show_counter == 'y':
            return alarm_with_timer(playfile, playfile_exists, hour, minute)
        else:
            return alarm(playfile, playfile_exists, hour, minute)

    except KeyboardInterrupt:
        return main()


#
#  name: alarm
#  @param sound object
#  @return main()
#
def alarm_with_timer(playfile, playfile_exists, hour, minute):
    try:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")

        nhour = int(current_time.strftime("%H"))
        nminute = int(current_time.strftime("%M"))
        nsec = int(current_time.strftime("%S"))

        nyear = int(current_time.strftime("%Y"))
        nmonth = int(current_time.strftime("%m"))
        nday = int(current_time.strftime("%d"))

        if (nhour * 60 * 60 + nminute * 60 + nsec) > (hour * 60 * 60 + minute * 60):
            #Next day
            day_shift = 1
        else:
            #same day
            day_shift = 0

        alarm_datetime = datetime.datetime(nyear, nmonth, nday + day_shift, hour, minute, 0)

        T = (alarm_datetime - current_time).total_seconds()
        t = int(T)

        hr, mn = divmod(t, 3600)
        mins, secs = divmod(mn, 60)

        if day_shift == 0:

            print("Alarm set for {0}:{1} in {2} hours {3} minutes and {4} seconds\n".format(hour, minute, hr, mins, secs))
        else:
            print("Alarm set for tomorrow at {0}:{1} in {2} hours {3} minutes and {4} seconds\n".format(hour, minute, hr, mins, secs))

        while True and t > 0:
                h, m = divmod(t, 3600)
                mins, secs = divmod(m, 60)
                print("{0}:{1}:{2}".format(h, mins, secs), end ='\r')
                time.sleep(1)
                t -= 1

        if playfile_exists:
            p = vlc.MediaPlayer(playfile)
            p.play()
        else:
            print("SILENT ALARM!")

        input("Sounding the alarm...")

        if playfile_exists:
            p.stop()

        r = input("Repeat countdown? (y/n): ")
        if r == 'y':
            return silent_countdown(playfile, playfile_exists, T)
        else:
            return main()

        if playfile_exists:
            p = vlc.MediaPlayer(playfile)
            p.play()
        else:
            print("SILENT ALARM!")

        input("Sounding the alarm...")

        if playfile_exists:
            p.stop()

        r = input("Repeat countdown? (y/n): ")
        if r == 'y':
            return alarm_with_timer(playfile, playfile_exists, hour, minute)
        else:
            return main()
    except KeyboardInterrupt:
        return main()


#
#  name: alarm
#  @param sound object
#  @return main()
#
def alarm(playfile, playfile_exists, hour, minute):
    try:
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")

        nhour = int(current_time.strftime("%H"))
        nminute = int(current_time.strftime("%M"))
        nsec = int(current_time.strftime("%S"))

        nyear = int(current_time.strftime("%Y"))
        nmonth = int(current_time.strftime("%m"))
        nday = int(current_time.strftime("%d"))


        if (nhour * 60 * 60 + nminute * 60 + nsec) > (hour * 60 * 60 + minute * 60):
            #Next day
            day_shift = 1
        else:
            #same day
            day_shift = 0

        alarm_datetime = datetime.datetime(nyear, nmonth, nday + day_shift, hour, minute, 0)

        T = (alarm_datetime - current_time).total_seconds()

        hr, mn = divmod(T, 3600)
        mins, secs = divmod(mn, 60)

        if day_shift == 0:
            print("Alarm set for {0}:{1} in {2} hours {3} minutes and {4} seconds\n".format(hour, minute, hr, mins, secs))
        elif day_shift == 1:
            print("Alarm set for tomorrow at {0}:{1} in {2} hours {3} minutes and {4} seconds\n".format(hour, minute, hr, mins, secs))
        else:
            print("Something is wrong")

        time.sleep(T)

        if playfile_exists:
            p = vlc.MediaPlayer(playfile)
            p.play()
        else:
            print("SILENT ALARM!")

        input("Sounding the alarm...")

        if playfile_exists:
            p.stop()

        r = input("Repeat countdown? (y/n): ")
        if r == 'y':
            return alarm(playfile, playfile_exists, hour, minute)
        else:
            return main()

    except KeyboardInterrupt:
        return main()

def Countdown_menu():
	cont_set_win = tk.Tk()
	cont_set_win.title("Countdown Timer Setup")
	cont_set_win.rowconfigure(0, minsize=400, weight=1)
	cont_set_win.columnconfigure(1, minsize=600, weight=1)
	
	
#
#  name: main
#  @param none
#  @return  function
#
def main():
    #Check if default playfile is set
    isFile = os.path.isfile(playfile)
    if isFile:
        default_playfile = True
    else:
        default_playfile = False
        print('Warning! No default playfile present!')

    choice = input("Press 'a' for alarm, 'c' for countdown timer, 's' for stopwatch, or 'x' to exit: ")

    if choice == 'a':
        return alarm_setup(playfile, default_playfile)
    elif choice == 'c':
        return countdown_setup(playfile, default_playfile)
    elif choice == 's':
        return stopwatch()
    elif choice == 'x':
        exit()
    else:
        main()


main()
