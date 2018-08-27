from tkinter import *
from tkinter import Menu, END, simpledialog, messagebox
import tkinter.scrolledtext as ScrolledText
import time
import datetime
from takvim import MyDatePicker
import os
from alarm import wAlarm
import sys
from Calculator import CalculatorOpen

pencere = Tk()
pencere.title("Notebook")
pencere.geometry("260x240+300+120")
pencere.resizable(False, False)

time2 = datetime.datetime.now()
today = time2.strftime(" %Y - %B - %d ")

def myNotes():

    file = r"Notes"
    if not os.path.exists(file):
        os.mkdir(file)

    def get_filenames():
        path = r"Notes"
        return os.listdir(path)

    root = Tk()
    root.title("My Notes")
    root.geometry("300x200+590+180")
    root.resizable(False, False)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    my_lists = Listbox(root, yscrollcommand=scrollbar.set)
    for filename in get_filenames():
        my_lists.insert(END, filename)

    my_lists.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=my_lists.yview)

    def notesOpen():
        text = Tk()
        text.resizable(False, False)
        index = my_lists.curselection()[0]
        openIndex = my_lists.get(index)
        file = open("Notes/" + str(openIndex),"r")

        textArea = ScrolledText.ScrolledText(text, width=100, height=30)
        textArea.pack()
        if file != None:
            contents = file.read()
            textArea.insert('1.0', contents)
            file.close()

        def againSave():
            messagebox.showinfo(title="Notes Save", message="Save is successfully")
            file = open("Notes/" + str(openIndex),"a")
            if file != None:
                data = textArea.get('1.0', END + '-1c')
                file.write(data)
                file.close()
        menu = Menu(text)
        text.config(menu=menu)
        menu.add_cascade(label="Save",command=againSave)

        text.mainloop()

    def delete():
        index = my_lists.curselection()[0]
        seltext = my_lists.get(index)
        my_lists.delete(index)
        os.remove(r"Notes/" + str(seltext))

    openButton = Button(root, text="Open Note", command=notesOpen)
    openButton.place(relx=.7, rely=.2, anchor="c")

    button2 = Button(root, text="Delete", command=delete)
    button2.place(relx=.7, rely=.6, anchor="c")

def newNote():
    # create child window
    root = Tk(className="Text Editor")
    root.resizable(False, False)
    textArea = ScrolledText.ScrolledText(root, width=100, height=30)
    textArea.pack()

    def findInFile():
        findString = simpledialog.askstring("Find...", "Enter Text")
        textData = textArea.get('1.0', END)

        occurances = textData.upper().count(findString.upper())

        if textData.upper().count(findString.upper()) > 0:
            label = messagebox.showinfo("Results", findString + " Has multiple occurances, " + str(occurances))
        else:
            label = messagebox.showinfo("Results", "Not Finded")

    def saveFile():
        # file = filedialog.asksaveasfile(mode='w',defaultextension=".txt", filetypes=(("Text file","*.txt"), ("All files","*.*")))
        root1 = Tk()
        root1.resizable(False, False)
        label = Label(root1,text="Write note name : ")
        label.pack()

        entry = Entry(root1)
        entry.pack()

        def filesave():
            if entry.get() != "":
                 messagebox.showinfo(title="Notes Save", message="Save is successfully")
                 file = open(r"Notes/" + str(entry.get()) + ".txt", "a")
                 if file != None:
                     data = textArea.get('1.0', END + '-1c')
                     file.write(data)
                     file.close()

            else:
                messagebox.showinfo(title="Wrong", message="Save is not success")
            #sys.exit(root)

        button = Button(root1, text="Save", command=filesave)
        button.pack()
        root1.mainloop()

    menu = Menu(root)
    root.config(menu=menu)
    fileMenu = Menu(menu)
    menu.add_cascade(label="Save", command=saveFile)
    menu.add_cascade(label="Find", command=findInFile)
    textArea.pack()
    # display message
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    root.mainloop()

clock = Label(pencere, font=('times', 20, 'bold'), bg='white')
clock.pack()

time1 = ''

def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)

tick()

def About():
    rAbout = Tk()
    rAbout.title("About")
    rAbout.resizable(False, False)
    rAbout.geometry("350x200+350+200")
    msg = Label(rAbout, text="This is Notebook app, you can write note, How can you use ?")
    msg.place(relx=.0, rely=.0)
    msg2 = Message(rAbout, text="Alarm : You should write Hours, Minutes and Seconds. İf your alarm is ten second you write "
                                "00 for hours, 00 for minutes, 10 for seconds.")
    msg2.place(relx=.0, rely=.2)
    msg3 = Message(rAbout, text="My Notes : You can see your notes. You can open and delete your notes.")
    msg3.place(relx=.5, rely=.2)

def Exit():
    sys.exit()

menu1 = Menu(pencere)
pencere.config(menu=menu1)
menuDosya = Menu(menu1, tearoff=0)
menu1.add_cascade(label="Options", menu=menuDosya)
menu1.add_cascade(label="About", command=About)
menuDosya.add_command(label="New Note", command=newNote)
menuDosya.add_command(label="Calendar", command=MyDatePicker)

frame1 = Frame(height=1, bd=2, relief=RIDGE)
frame1.pack(fill=X, pady=6, padx=6, side=TOP)

etiket1 = Label(frame1, text="Year - Month - Day :       " + today)
etiket1.pack(side=LEFT)

button = Button(pencere, text="My Notes", height="2", width="8", command=myNotes)
button.place(relx=.3, rely=.5, anchor="c")

button2 = Button(pencere, text="Calculator", height="2", width="8", command=CalculatorOpen)
button2.place(relx=.7, rely=.5, anchor="c")

alarmButton = Button(pencere, text="Alarm", height="2", width="8", command=wAlarm)
alarmButton.place(relx=.3, rely=.8, anchor="c")

exitButton = Button(pencere, text="Exit", height="2", width="8", command=Exit)
exitButton.place(relx=.7, rely=.8, anchor="c")

mainloop()
