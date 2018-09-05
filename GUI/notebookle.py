# -*- encoding: utf8 -*-
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
filename = ''


def new():
    pass


def openfile():
    global filename
    filename = filedialog.askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title('Filename:'+os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read().encode())
        f.close()


def savefile():
    pass


def savefile2():
    pass


def back():
    pass


def repeat():
    pass


def copy():
    pass


def load():
    pass


def cutdown():
    pass


def choseall():
    pass


def find():
    pass


def author():
    messagebox.showinfo("作者信息", "姓名：欧阳文明\n性别：男")


def about():
    messagebox.showinfo("版权copyright", '版权归欧阳文明享有')


root = Tk()
root.title('新世界')
root.geometry('1000x600+450+100')
# 创建一个菜单栏
menubar = Menu(root)
root.config(menu=menubar)
# 在菜单栏中创建文件菜单
filemenu = Menu(menubar)
# 在文件菜单中添加选项 accelerator表示快捷键
filemenu.add_command(label='新建', accelerator='Ctrl+N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl+O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl+S', command=savefile)
filemenu.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=savefile2)
# 将文件菜单添加到菜单栏中去
menubar.add_cascade(label='文件', menu=filemenu, accelerator='Ctrl+a')

# 在菜单栏中创建编辑菜单
editmenu = Menu(menubar)
# 在编辑菜单中添加选项
editmenu.add_command(label='撤销', accelerator='Ctrl+Z', command=back)
editmenu.add_command(label='重做', accelerator='Ctrl+Y', command=repeat)
editmenu.add_separator()
editmenu.add_command(label='复制', accelerator='Ctrl+C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl+V', command=load)
editmenu.add_command(label='剪切', accelerator='Ctrl+X', command=cutdown)
editmenu.add_separator()
editmenu.add_command(label='全选', accelerator='Ctrl+A', command=choseall)
editmenu.add_command(label='查找', accelerator='Ctrl+F', command=find)
# 将编辑菜单加入到菜单栏中去
menubar.add_cascade(label='编辑', menu=editmenu)

# 在菜单栏中创建关于
aboutmenu = Menu(menubar)
aboutmenu.add_command(label='作者', command=author)
aboutmenu.add_command(label='版权', command=about)
menubar.add_cascade(label='关于', menu=aboutmenu)

# 创建工具栏
# 工具栏颜色
toolbar = Frame(root, height=25, bg='light sea green')
# 工具栏位置
toolbar.pack(expand=NO, fill=X)
# 打开按钮
shortbutton = Button(toolbar, text='打开', command=openfile)
shortbutton.pack(side=LEFT, padx=5, pady=5)
# 保存按钮
shortbutton = Button(toolbar, text='保存')
shortbutton.pack(side=LEFT, padx=5, pady=5)

# 创建状态栏
statusbar = Label(root, text='我是状态栏', bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# 行号实现
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)
# 编辑区
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

# 滚动条
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)
root.mainloop()
