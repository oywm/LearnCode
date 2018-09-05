from tkinter import *
from tkinter import messagebox

root = Tk()
Label(root, text='账号：').grid(row=0)
Label(root, text='密码：').grid(row=1)


def callback():
    if messagebox._show(message='您好，登陆成功'):
        message = e1.get()
        print(message)
        print('欢迎进入游戏')


e1 = Entry(root)
e1.grid(row=0, column='1')

e2 = Entry(root)
e2.grid(row=1, column='1')

button = Button(root, text='登陆', command=callback)
button.grid(row=2)
root.mainloop()

