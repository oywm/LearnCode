from tkinter import *

root = Tk()


def callback():
    print('clicked tool bar button')


tool_bar = Frame(root)
b = Button(tool_bar, text='new', width=6, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

c = Button(tool_bar, text='open', width=6, command=callback)
c.pack(side=LEFT, padx=2, pady=2)

tool_bar.pack(side=TOP, fill=Y)
root.mainloop()
