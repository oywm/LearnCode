import tkinter as tk

win = tk.Tk()
win.title('haha')
win.geometry("400x400+800+200")


def func():
    print('sunck is a good man!')


button = tk.Button(win, text='按钮', command=func, width=5, height=2)

button.pack()
tk.mainloop()
