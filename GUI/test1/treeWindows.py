import tkinter
from tkinter import ttk
import os


class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, othewin):
        frame = tkinter.Frame(master)
        frame.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.otherwin = othewin
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)

        root = self.tree.insert('', 'end', text=self.get_last_path(path), open=True, values=path)

        self.loadTree(root, path)

        self.scroll = tkinter.Scrollbar(frame)
        self.scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scroll.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scroll.set)

        self.tree.bind("<<TreeviewSelect>>", self.func)

    def func(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)['text']
            self.otherwin.ev.set(file)
            apath = self.tree.item(sv)['values'][0]
            print(apath)

    def loadTree(self, parent, parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath, fileName)
            treey = self.tree.insert(parent, 'end', text=self.get_last_path(absPath), values=absPath)
            if os.path.isdir(absPath):
                self.loadTree(treey, absPath)

    def get_last_path(self, path):
        path = path.split('\\')[-1]
        return path
