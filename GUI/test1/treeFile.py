import tkinter
import os
from test1.treeWindows import TreeWindows
from test1.infoWindows import InfoWindows
win = tkinter.Tk()
win.title('haha')
win.geometry('800x400+600+200')

path = 'D:\python工作空间'

infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)


tkinter.mainloop()

