import tkinter as tk
#
# win = tk.Tk()
#
# win.title('haha')
# win.geometry("400x400+800+400")
#
# label = tk.Label(win, text='sunck is a good man',
#                  bg='pink',
#                  fg='red')
# label.pack()
#
# win.mainloop()


win = tk.Tk()
win.title('asd')
win.geometry("400x400+800+400")
fr1 = tk.Frame(win)
fr1.grid(row=0, column=1)
fr1.pack(side=tk.LEFT, fill=tk.Y)
label1 = tk.Label(fr1, text='sunck is a good man' )
label1.pack()


fr2 = tk.Frame(win)
fr2.pack()
label2 = tk.Label(fr2, text='sunck is a good man!' )
label2.pack()

tk.mainloop()
