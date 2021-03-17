'''
Nicholas Zehm
Pytimer.py
3-12-21

Very simple countdown timer script. Requires the vlc python module. Manually set the default sound for your system.
Version 1.1
Add hours, deal with negative values (the script worked with negative values, due to the t > 0 check) 
'''

import time
import os   #for path to music/sound
import vlc  #this module is from the vlc team, and is required for music/sound


def countdown():
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
    
    #### EDIT THIS: provide a valid file (vlc usable) for playfile. This will be used as default/fallback ####
    playfile = "/media/phosphorus/Internal Backup/Gaming Computer/Music/kid kudi.wav"
    
    if a == 'y':
        path = input("Input sound file directory (no ""s): ")

        isFile = os.path.isfile(path)
        if isFile == True:
            playfile = path
            print("Using {0}".format(playfile))
        else:
            print("Error: Using default sound.")
            
    t = h * 60 * 60 + m * 60 + s

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
        pass
        
countdown()   
