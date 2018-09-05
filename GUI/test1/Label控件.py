import tkinter as tk

win = tk.Tk()
win.title('哈哈')
win.geometry("400x400+800+200")
label = tk.Label(text='sunck is a good man!',
                 bg='pink',
                 fg='red',
                 font=('黑体', 20),
                 )

# label 显示
label.pack()

win.mainloop()

