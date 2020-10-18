import tkinter
import os
from tkinter import *

from tkinter.messagebox import *

from tkinter.filedialog import *


class Notepad:
    _root = Tk()

    _thisWidth = 300
    _thisHeight = 300
    _thisTextArea = Text(_root)
    _thisMenuBar = Menu(_root)
    _thisFileMenu = Menu(_thisMenuBar, tearoff=0)
    _thisEditMenu = Menu(_thisMenuBar, tearoff=0)
    _thisHelpMenu = Menu(_thisMenuBar, tearoff=0)

    _thisScrollBar = Scrollbar(_thisTextArea)
    _file = None

    def __init__(self, **kwargs):

        try:
            self._root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self._thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self._thisHeight = kwargs['height']
        except KeyError:
            pass

        self._root.title("Untitled - AKASH")

        screenWidth = self._root.winfo_screenmmwidth()
        screenHeight = self._root.winfo_screenheight()

        left = (screenWidth / 2) - (self._thisWidth / 2)
        top = (screenHeight / 2) - (self._thisHeight / 2)

        self._root.geometry('%dx%d+%d+%d' % (self._thisWidth, self._thisHeight, left, top))

        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)

        self._thisTextArea.grid(sticky=N + E + S + W)

        self._thisFileMenu.add_command(label="New", command=self._newFile)
        self._thisFileMenu.add_command(label="Open", command=self._openFile)
        self._thisFileMenu.add_command(label="Save", command=self._saveFile)

        self._thisFileMenu.add_separator()
        self._thisFileMenu.add_command(label="Exit", command=self._quitApplication)
        self._thisMenuBar.add_cascade(label="File", menu=self._thisFileMenu)

        self._thisEditMenu.add_command(label="Cut", command=self._cut)
        self._thisEditMenu.add_command(label="Copy", command=self._copy)
        self._thisEditMenu.add_command(label="Paste", command=self._paste)

        self._thisMenuBar.add_cascade(label="Edit", menu=self._thisEditMenu)

        self._thisHelpMenu.add_command(label="About Notepad", command=self._showAbout)
        self._thisMenuBar.add_cascade(label="Help", menu=self._thisHelpMenu)

        self._root.config(menu=self._thisMenuBar)

        self._thisScrollBar.pack(side=RIGHT, fill=Y)

        self._thisScrollBar.config(command=self._thisTextArea.yview)
        self._thisTextArea.config(yscrollcommand=self._thisScrollBar.set)

    def _quitApplication(self):
        self._root.destroy()

    def _showAbout(self):
        showinfo("NotePad", "HJHSDJSDH")

    def _openFile(self):

        self._file = askopenfilename(defaultextension=".txt",
                                     filetypes=[("ALL FILES", "*.*"),
                                                ("Text Documents", "*.txt")])

        if self._file == "":

            self._file = None
        else:
            self._root.title(os.path.basename(self._file) + " - No")
            self._thisTextArea.delete(1.0, END)

            file = open(self._file, "r")
            self._thisTextArea.insert(1.0, file.read())

            file.close()

    def _newFile(self):
        self._root.title("Untitled - Notepad")
        self._file = None
        self._thisTextArea.delete(1.0, END)

    def _saveFile(self):
        if self._file is None:
            self._file = asksaveasfilename(initialfile='Untitled.txt',
                                           defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt")])

            if self._file == "":
                self._file = None
            else:

                file = open(self._file, "w")
                file.write(self._thisTextArea.get(1.0, END))
                file.close()

                self._root.title(os.path.basename(self._file))

        else:
            file = open(self._file, "w")
            file.write(self._thisTextArea.get(1.0, END))
            file.close()

    def _cut(self):
        self._thisTextArea.event_generate("<<Cut>>")

    def _copy(self):
        self._thisTextArea.event_generate("<<Copy>>")

    def _paste(self):
        self._thisTextArea.event_generate("<<Paste>>")

    def run(self):

        self._root.mainloop()


notepad = Notepad(width=600, height=400)
notepad.run()
