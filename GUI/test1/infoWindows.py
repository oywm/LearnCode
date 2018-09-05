import tkinter
from tkinter import ttk
import os


class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.RIGHT)

        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame, textvariable=self.ev)
        self.entry.pack(side=tkinter.TOP)

        self.txt = tkinter.Text(frame)
        self.txt.pack(side=tkinter.BOTTOM)
