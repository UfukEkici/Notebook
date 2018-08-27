import tkinter
import time
import winsound
import math
from tkinter import messagebox

def wAlarm():
    def countdown(count):
        seconds = math.floor(count&60)
        minutes = math.floor((count/60)%60)
        hours = math.floor((count/3600))
        label['text'] ="Hours: "+ str(hours)+ "Minutes:  " +str(minutes)+ " Seconds: " +str(seconds)

        if count >= 0:
            top.after(1000, countdown,count-1)
        else:
            for x in range(1):
                winsound.Beep(1000,1000)
                label['text']="Time is up!"
                messagebox.showinfo("Wrong", "Time is up!")

    def updateButton():
        hour,minute,sec=hoursE.get(),minuteE.get(),secondE.get()
        if hour.isdigit() and minute.isdigit() and sec.isdigit():
            time=int(hour)*3600+int(minute)*60+int(sec)
            countdown(time)

    top = tkinter.Tk()
    top.geometry("250x150+500+230")
    top.resizable(False, False)
    hoursT=tkinter.Label(top, text="Hours:")
    hoursE=tkinter.Entry(top)
    minuteT=tkinter.Label(top, text="Minutes:")
    minuteE=tkinter.Entry(top)
    secondT=tkinter.Label(top, text="Seconds:")
    secondE=tkinter.Entry(top)
    hoursT.grid(row=1,column=1)
    hoursE.grid(row=1,column=2)
    minuteT.grid(row=2,column=1)
    minuteE.grid(row=2,column=2)
    secondT.grid(row=3,column=1)
    secondE.grid(row=3,column=2)
    label = tkinter.Label(top)
    label.grid(row=5,column=2)

    button=tkinter.Button(top,text="Start Timer",command=updateButton)
    button.grid(row=4,column=2)

    top.mainloop()