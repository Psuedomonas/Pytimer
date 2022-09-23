devlog.md
Consider using multithreading for multiple clocks.
	- KIS method might be better for now. Just get alarm clocks working...
	
Rejected code (for now)
#import re   #For matching repeat alarm days
    '''
    r = input("repeat alarm? (y/n): ")
    if r == 'y':
        repeat = True
        d = input("day(s) (format MoTuWeThFrSaSu or All): ")
        pMonday = "Mo"
        pTuesday = "Tu"
        pWednesday = "We"
        pThursday = "Th"
        pFriday = "Fr"
        pSaturday = "Sa"
        pSunday = "Su"
        pAll = "all | All | ALL"

        Mon = re.match(d, pMonday)
        Tue = re.match(d, pTuesday)
        Wed = re.match(d, pWednesday)
        Thu = re.match(d, pThursday)
        Fri = re.match(d, pFriday)
        Sat = re.match(d, pSaturday)
        Sun = re.match(d, pSunday)
        All = re.match(d, pAll)

        if All:
            pass
        elif Mon:
            pass
        elif Tue:
            pass
        elif Wed:
            pass
        elif Thu:
            pass
        elif Fri:
            pass
        elif Sat:
            pass
        elif Sun:
            pass

    else:
        repeat = False
    '''

   '''
    T = 0
    time.sleep(T)

    p = vlc.MediaPlayer(playfile)
    p.play()
    '''
