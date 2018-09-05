from tkinter import *


def callback():
    print("call the menu")


root = Tk()
root.frame
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New', command=callback)
file_menu.add_command(label='Open..', command=callback)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=callback)

help_menu = Menu(menu)
menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About..', command=callback)

root.mainloop()

