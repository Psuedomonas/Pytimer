'''
From code at https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
'''
# import the time module 
import time 
from playsound import playsound

inputTime = array('B')


def getTime():
    badInputs = 0
    while badInputs < 4:
        try:
            h = int(input("Hours: "))
            m = int(input("Minutes: "))
            s = int(input("Seconds: "))
        except:
            print("Not valid input")
            badInputs += 1
        else:
            print("we ran successfully")
               
            

'''  

def countdown():
    
    gettime()
    
    alarm = input("Enter sound file, or leave blank for no sound: ")
    #Check if is a legit directory
    
    if hrs == 0:
        while t:
            mins, secs = divmod(t, 60) 
            print("{:02d}:{:02d}".format(mins, secs)
            time.sleep(1)
            t -= 1
            
        print("Sounding the alarm...")
        playsound(alarm)
    else
        print("I haven't finished this yet!")


        
def ftimer:
    pass
        
        
while not t == 'x':
    t = input("Type c for countdown, t for timer, x to exit")
    
    if t = 'c':
        countdown()
    elif t = 't':
        ftimer
    else
        pass    

# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Fire in the hole!!') 
  
  
# input time in seconds 
t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(t)) 
'''
getTime()
