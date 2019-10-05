from Tkinter import *
import ttk
from tkinter import PhotoImage
import os

root = Tk()
tree = ttk.Treeview()
tree["columns"]=("one","two")
tree.column("one", width=100 )
tree.column("two", width=100)

tree.heading("#0", text="Name")
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("" , 0,    text="Line 1", values=("1A","1b"))

imgFolder = PhotoImage(file="Folder.gif")
imgFile = PhotoImage(file="File.gif")

id2 = tree.insert("", 1, "dir2", text="Dir 2", image=imgFolder)
tree.insert(id2, "end", "dir 2", text="sub dir 2", image=imgFile)

##alternatively:
#tree.insert("", 3, "dir3", text="Dir 3")
#tree.insert("dir3", 3, text=" sub dir 3")

tree.pack()
root.mainloop()