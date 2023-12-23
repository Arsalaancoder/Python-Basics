import winsound
import time
import pyttsx3    
def Beep_alarm():
    for repeats in range(7):
        winsound.Beep(3000,500)
        winsound.Beep(6000,300)
timeDuration=int(input("duration in seconds:"))
hours,minutes,seconds=0,0,0
for i in range(timeDuration):
    print('\n'*100)
    seconds+=1
    if seconds==60:
        minutes+=1
        seconds=0
    if minutes==60:
        hours+=1
        minutes=0
    print(str(hours)+":"+str(minutes)+":"+str(seconds))
    time.sleep(1)
if __name__ == '__main__':
    Beep_alarm()
vtf=pyttsx3.init()
rate = vtf.getProperty('rate')
vtf.setProperty('rate', 140)    
def vtf_speak(text):
    vtf.say(text)
    vtf.runAndWait()
txt="your time is up"
print(txt.upper())
vtf_speak(txt)