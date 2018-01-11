import tkinter
from tkinter import messagebox


class Console():
    def __init__(self, master):
        self.__master = master
        self.__master.geometry("200x100")

        self.__start = tkinter.Button(self.__master, text="Zi-le, Guta!", command=self.createGrid)
        self.__start.pack()

    def showHello(self):
        messagebox.showinfo("test", "Hello lumeee!")

    def createGrid(self):
        self.__start.pack_forget()
        btn1 = tkinter.Button(self.__master, text="1")
        btn1.grid(row=0, column=0)

