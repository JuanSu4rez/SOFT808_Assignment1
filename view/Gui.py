from Tkinter import *
import tkFileDialog
from tkinter import PhotoImage
import ttk


from pathlib import Path
import os
import docx2txt


class Gui(Frame):

    myController = None

    def __init__(self, master):
        print "constructor view"
        Frame.__init__(self, master)
        self.master.title("Folder Maker")
        self.master.geometry("1100x650")
        self.master.resizable(width=None, height=None)

        #Panel "Upload a Word file"
        self.frmUploadFile = Frame(height=90, width=700, bd=3, relief='groove').place(x=5, y=10)
        self.lblLoadFile = Label(master, text="Upload a Word file").place(x=15, y=0)
        self.txtFilePath = Entry(master, text="", width=100).place(x=15, y=30)
        self.btnUploadFile = Button(master, text="Browse...", width=8, command=self.uploadFile).place(x=625, y=25)
        self.btnReadFile = Button(master, text="Read file", width=8, command=self.readFile).place(x=310, y=60)

        #Panel "Setting values"
        self.frmFileName = Frame(height=170, width=700, bd=3, relief='groove').place(x=5, y=110)
        self.lblPnlSettingValues = Label(master, text="Setting values").place(x=15, y=100)
        self.lblSemester = Label(master, text="Semester").place(x=15, y=120)
        self.txtSemester = Entry(master, text="", width=12).place(x=15, y=150)
        self.lblYear = Label(master, text="Year").place(x=100, y=120)
        self.txtYear = Entry(master, text="", width=12).place(x=100, y=150)
        self.lblCourseCode = Label(master, text="Course code").place(x=185, y=120)
        self.txtCourseCode = Entry(master, text="", width=12).place(x=185, y=150)
        self.lblFolderName = Label(master, text="Folder name").place(x=270, y=120)

        self.txtFolderName = Entry(master, text="", width=70, state=DISABLED)
        self.txtFolderName.place(x=270, y=150)

        self.lblDestination = Label(master, text="Select folder destination").place(x=15, y=180)

        self.txtFolderPath = Entry(master, text="", width=100)
        self.txtFolderPath.place(x=15, y=210)

        self.btnSelectDestination = Button(master, text="Browse...", width=8, command=self.selectDestination)
        self.btnSelectDestination.place(x=625, y=205)

        self.btnGenerate = Button(master, text="Generate", width=8, state=DISABLED, command=self.generate)
        self.btnGenerate.place(x=310, y=240)

        #Panel "Folder structure"
        self.imgFolder = PhotoImage(file="./Folder.gif")
        self.imgFile = PhotoImage(file="./File.gif")

        self.frmTree = Frame(height=280, width=700, bd=3, relief='groove').place(x=5, y=290)
        self.lblFolderStructure = Label(master, text="Folder structure").place(x=15, y=280)
        self.viewTree = ttk.Treeview(master, height=11)
        self.viewTree.place(x=10, y=300)
        #tree.place(x=310, y=240)

        #GUI attributes
        self.strPathSelectedFile = ""
        self.strPathSelectedFolder = ""
        self.strFolderName = ""

        #TODO - FIX PATHS TO ICON FILES

        # self.pack()

    def setController(self, param):
        self.myController = param

    def disablePnlNameFolder(self):
        self.txtSemester["state"] = "disabled"
        self.txtYear["state"] = "disabled"
        self.txtCourseCode["state"] = "disabled"

    def enablePnlNameFolder(self):
        self.txtSemester["state"] = "enable"
        self.txtYear["state"] = "enable"
        self.txtCourseCode["state"] = "enable"

    def disablebtnGenerate(self):
        self.btnGenerate["state"] = "disabled"

    def enablebtnGenerate(self):
        self.btnGenerate["state"] = "active"

    def drawTree(self):
        tree = self.viewTree

        tree["columns"] = ("one", "two")
        tree.column("#0", width=285, minwidth=270, stretch=NO)
        #tree.column("one", width=150, minwidth=150, stretch=NO)


        tree.heading("#0", text="Name")
        #tree.heading("one", text="Date modified")

        id2 = tree.insert("", 1, "dir2", text=" Folder 1", image=self.imgFolder)
        tree.insert(id2, "end", "dir 2", text=" File 1", image=self.imgFile)


    def uploadFile(self):
        print "upload file GUI"
        self.strPathSelectedFile = tkFileDialog.askopenfile(title="Select a Word file", filetypes=[('Word file', '*.docx')])
        # pathFile = tkFileDialog.askopenfile(title="Select a Word file", filetypes=[('Word file', '*.docx')])
        # if pathFile is not None:
        #    return pathFile
        # else:
        #    return None

    def readFile(self):
        print "readFile"

    def generate(self):
        print "generateFile() GUI"
        self.myController.generateFolders()

    def selectDestination(self):
        self.strPathSelectedFolder = tkFileDialog.askdirectory(title="Select the folder destination")
        self.myController.updateFolderDestination()

    def setPathloadedFile(self, param):
        self.txtFilePath.insert(0, param)

    def setPathDestination(self, param):
        self.txtFolderPath.delete(0, END)
        self.txtFolderPath.insert(0, param)