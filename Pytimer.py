'''
Nicholas Zehm
Pytimer.py
2-27-21

Very simple timer script. Requires the vlc python module. Manually set the default sound for your system.
'''

import time
import os   #for path to music/sound
import vlc  #this module is from the vlc team, and is required for music/sound

def countdown():
    m = int(input("minutes: "))
    s = int(input("seconds: "))
    a = input("User defined alarm sound? y/n: ")
    
    #### EDIT THIS: provide a valid file (vlc usable) for playfile ####
    playfile = ""

    if a == 'y':
        path = input("Input sound file directory (no ""s): ")

        isFile = os.path.isfile(path)
        if isFile == True:
            playfile = path
            print("Using {0}".format(playfile))
        else:
            print("Error: Using default sound.")
    t = m*60 + s

    #Ctrl-C causes KeyboardInterrupt to be raised
    try:
        while True and t > 0:
            mins, secs = divmod(t, 60) 
            print("{:02d}:{:02d}".format(mins, secs), end ='\r')
            time.sleep(1)
            t -= 1
        p = vlc.MediaPlayer(playfile)
        p.play()
        input("Sounding the alarm...")        
    except KeyboardInterrupt:
        pass
        
countdown()   
