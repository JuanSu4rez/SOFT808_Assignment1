from Tkinter import *
import tkFileDialog
from tkinter import PhotoImage
import ttk
from pathlib import Path
import os


from pathlib import Path
import os
import docx2txt

#   SOFT808 Software User Experience
#   Juan Sebastian Suarez
#   View - Main frame

class Gui(Frame):


    myController = None
    strPathSelectedFile = ""
    semesterOption = None
    yearOption = None


    def __init__(self, master):
        print "constructor view"
        self.semesterOption = StringVar()
        self.yearOption = StringVar()
        Frame.__init__(self, master)
        self.master.title("Course outline creator")
        self.master.configure(background='#66CCCC')
        self.master.geometry("1100x650")
        self.master.resizable(width=None, height=None)

        #Panel "Upload a Word file"
        self.frmUploadFile = Frame(height=90, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=10)
        self.lblLoadFile = Label(master, text="Upload a Word file", bg='#66CCCC', font="Verdata 12").place(x=15, y=0)

        self.txtFilePath = Entry(master, text="", width=100)
        self.txtFilePath.place(x=15, y=30)

        self.btnUploadFile = Button(master, text="Browse...", fg='#990000', font="Verdata 10 bold", width=8, command=self.uploadFile).place(x=625, y=25)
        self.btnReadFile = Button(master, text="Read file", bg='#DB0000', fg='#FFFFFF', font="Verdata 10 bold", width=8, command=self.readFile).place(x=310, y=60)

        #Panel "Setting values"
        self.frmFileName = Frame(height=170, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=110)
        self.lblPnlSettingValues = Label(master, text="Setting values", fg='#990000', bg='#66CCCC', font="Verdata 12 bold").place(x=15, y=100)
        self.lblSemester = Label(master, text="Semester", bg='#66CCCC', font="Verdata 11").place(x=15, y=120)

        semesterOptions = ["S1", "S2", "S3"]

        self.semesterComboBox = ttk.Combobox(master, textvariable =self.semesterOption, values=semesterOptions)
        self.semesterComboBox.config(width=8)
        self.semesterComboBox.place(x=15, y=150)
        self.semesterComboBox.set(semesterOptions[0])
        self.semesterComboBox.bind("<<ComboboxSelected>>", self.updadeFileName)

        self.lblYear = Label(master, text="Year", bg='#66CCCC', font="Verdata 11").place(x=100, y=120)

        yearOptions = []
        for x in range(2000, 2050):
            yearOptions.append(str(x) + "")

        self.yearComboBox = ttk.Combobox(master, textvariable =self.yearOption, values=yearOptions)
        self.yearComboBox.config(width=8)
        self.yearComboBox.place(x=100, y=150)
        self.yearComboBox.set(yearOptions[0])
        self.yearComboBox.bind("<<ComboboxSelected>>", self.updadeFileName)

        self.lblCourseCode = Label(master, text="Course code", bg='#66CCCC', font="Verdata 11").place(x=180, y=120)

        self.txtCourseCode = Entry(master, text="", width=12, state='readonly')
        self.txtCourseCode.place(x=185, y=150)
        self.txtCourseCode.bind("<Key>", self.updadeFileName)

        self.lblFolderName = Label(master, text="Folder name", bg='#66CCCC', font="Verdata 11").place(x=270, y=120)

        self.txtFolderName = Entry(master, text="", width=70, state='readonly')
        self.txtFolderName.place(x=270, y=150)

        self.lblDestination = Label(master, text="Select folder destination", bg='#66CCCC', font="Verdata 11").place(x=15, y=180)

        self.txtFolderPath = Entry(master, text="", width=100)
        self.txtFolderPath.place(x=15, y=210)

        self.btnSelectDestination = Button(master, text="Browse...", borderwidth=2, relief=SOLID, font="Verdata 10 bold", width=8, command=self.selectDestination)
        self.btnSelectDestination.place(x=625, y=205)

        self.btnGenerate = Button(master, text="Generate", bg='#39369C', fg='#FFFFFF', font="Verdata 12", width=8, state=DISABLED, command=self.generate)
        self.btnGenerate.place(x=310, y=240)

        #Panel "Folder structure"

        #Tree
        self.frmTree = Frame(height=280, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=290)
        self.lblFolderStructure = Label(master, text="Folder structure", bg='#66CCCC', font="Verdata 11").place(x=15, y=280)
        self.viewTree = ttk.Treeview(master, height=11)
        self.viewTree.place(x=10, y=300)
        #tree.place(x=310, y=240)

        #Panel Instructions



        self.imgLogo = PhotoImage(file="./Logo.gif")
        self.lblImgLogo = Label(master, image=self.imgLogo)
        self.lblImgLogo.pack()
        self.lblImgLogo.place(x=825, y=10)

        self.imgInstructions = PhotoImage(file="./Instructions.gif")
        self.lblImgInstructions = Label(master, image=self.imgInstructions)
        self.lblImgInstructions.pack()
        self.lblImgInstructions.place(x=775, y=185)

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

        #tree["columns"] = ("one", "two")
        #tree.column("#0", width=285, minwidth=270, stretch=NO)
        #tree.column("one", width=150, minwidth=150, stretch=NO)

        #tree.heading("#0", text="Name")
        ##tree.heading("one", text="Date modified")

        #id2 = tree.insert("", 1, "dir2", text=" Folder 1", image=self.imgFolder)
        #tree.insert(id2, "end", "dir 2", text=" File 1", image=self.imgFile)


    def uploadFile(self):
        print "upload file GUI"
        pathSelectedFile = tkFileDialog.askopenfile(title="Select a Word file", filetypes=[('Word file', '*.docx'), ('Word file', '*.doc')])
        if pathSelectedFile is not None:
            self.myController.uploadFile(pathSelectedFile.name)

    def readFile(self):
        self.myController.readFile()

    def generate(self):
        self.myController.generateFolders()

    def selectDestination(self):
        self.strPathSelectedFolder = tkFileDialog.askdirectory(title="Select the folder destination")
        self.myController.updateFolderDestination()

    def setPathloadedFile(self, param):
        self.txtFilePath.insert(0, param)

    def setPathDestination(self, param):
        self.txtFolderPath.delete(0, END)
        self.txtFolderPath.insert(0, param)

    def updadeFileName(self, event):
        self.myController.updadeFolderNameToGenerate()
