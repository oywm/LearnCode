from tkinter import *
from tkinter import messagebox
root = Tk()


def callback():
    if messagebox.askokcancel('完美世界', '欧哥，你好，现在进入游戏嘛？'):
        print('Yes')
    else:
        print('No')


button = Button(root, text='Button1', command=callback)
button.pack()
root.mainloop()
