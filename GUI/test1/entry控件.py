import tkinter as tk

win = tk.Tk()
win.title('haha')
win.geometry("400x400+800+200")

entry = tk.Entry(win, show='*')
entry.pack()

tk.mainloop()
