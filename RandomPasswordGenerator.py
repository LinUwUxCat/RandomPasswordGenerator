from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

def newpass():

    def createpassword():
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&é(-è_çà°)=+~#[]|^@$£*µù%!§:/;.,?<>²1234567890"
        global yourpass
        yourpass = ""
        for i in range(0, recup):
            yourpass = yourpass + random.choice(characters)
        mainwin.clipboard_clear()
        mainwin.clipboard_append(yourpass)
        messagebox.showinfo("Password Created!", "Your password has been copied to your clipboard.")

        
    def ok():
        global recup
        recup = int(tkinput.get())
        numcharwin.destroy()
        createpassword()

    numcharwin = tk.Tk()
    numcharwin.title("Password Length...")
    number = IntVar() 
    number.set(0)
    numonly = Label(numcharwin, text = "Enter the length of your password (numbers only please!)\n")
    numonly.pack()
    tkinput = Entry(numcharwin, textvariable=number, width=30)
    tkinput.pack()
    validatebutton = Button(numcharwin, text = "OK", command = ok)
    validatebutton.pack()
    numcharwin.mainloop()



mainwin = tk.Tk()
mainwin.title("Random Password Generator")
mainwin.geometry("200x100")
presentation = Label(mainwin, text = "Random Password Generator")
presentation.pack()
newpassbutton = tk.Button(mainwin, text = "New Password...", command = newpass)
newpassbutton.place(x = 30, y = 40)
mainwin.mainloop()

