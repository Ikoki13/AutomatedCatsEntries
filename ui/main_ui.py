from tkinter import Tk

import customtkinter

from Classes import CATsRow

def copyTimeFromEntry(timeEntries, index):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(timeEntries[index-1].duration)
    r.update()  # now it stays on the clipboard after the window is closed


def copyTextFromEntry(timeEntries, index):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    #r.clipboard_append(timeEntries[index-1].cellText)
    print("index: " + str(index))

    r.update()  # now it stays on the clipboard after the window is closed


def drawCATsTimetable(catsRow: CATsRow) -> CATsRow:
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    # Setup root
    root = customtkinter.CTk()
    root.title = "CATs Entries"
    root.geometry("800x400")
    # root.resizable(0, 0)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(2, weight=7)
    root.columnconfigure(3, weight=1)

    timeLabel = customtkinter.CTkLabel(master=root, text="Duration")
    timeLabel.grid(row=0, column=0, padx=20, pady=10)

    textLabel = customtkinter.CTkLabel(master=root, text="Text")
    textLabel.grid(row=0, column=1, columnspan=2, padx=20, pady=10)

    timeEntries = catsRow.getListOfTimeEntries()

    i = 1
    for e in timeEntries:
        timeEntryLabel= customtkinter.CTkLabel(master=root, text=e.duration)
        timeEntryLabel.grid(row=i, column=0)
        textEntryLabel = customtkinter.CTkLabel(master=root, text=e.cellText, justify="left")
        textEntryLabel.grid(row=i, column=1)
        textButton = customtkinter.CTkButton(master=root, text="Copy", command=lambda: copyTextFromEntry(timeEntries, i))
        textButton.grid(row=i, column=2)
        i = i+1

    root.mainloop()
