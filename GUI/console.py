import tkinter
from tkinter import messagebox


class Console():
    def __init__(self, master):
        self.__master = master
        self.__master.geometry("200x100")

        self.__butt = tkinter.Button(master, text="Zi-le, Guta!", command=self.showHello)
        self.__butt.pack()

    def showHello(self):
        messagebox.showinfo("test", "Hello lumeee!")