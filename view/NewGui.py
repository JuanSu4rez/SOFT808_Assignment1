from tkinter import *
import tkFileDialog
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from pathlib import Path
import os


from pathlib import Path
import os
import docx2txt


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
        self.master.title("Folder Maker")
        self.master.configure(background='#66CCCC')
        self.master.geometry("800x650")
        self.master.resizable(width=None, height=None)

        #Panel "Upload a Word file"
        self.lblLoadFile = Label(master, text="Upload a Word file",bg='#66CCCC',font="Verdata 12").place(x=40, y=10)
        self.txtFilePath = Entry(master, text="", font="15", width=32)
        self.txtFilePath.place(x=40, y=40)

        self.btnUploadFile = Button(master, text="Browse...",fg='#990000',font="Verdata 10 bold", width=9, command=self.uploadFile).place(x=340, y=38)
        self.btnReadFile = Button(master, text="Upload", width=9,bg='#DB0000',fg='#FFFFFF',font="Verdata 10 bold").place(x=430, y=38)

        #Panel "Setting values"
        self.frmFileName = Frame(height=170, width=500,bd=3, relief='groove',background='#66CCCC').place(x=30, y=80)
        self.lblSemester = Label(master,text="Set Values",fg='#990000',bg='#66CCCC',font="Verdata 12 bold").place(x=40, y=70)

        semesterOptions = ["S1", "S2", "S3"]

        self.semesterComboBox = ttk.Combobox(master, textvariable =self.semesterOption, values=semesterOptions)
        self.semesterComboBox.config(width=10,font="13")
        self.semesterComboBox.place(x=40, y=110)
        self.semesterComboBox.set(semesterOptions[0])
        self.semesterComboBox.bind("<<ComboboxSelected>>", self.updadeFileName)

        self.lblYear = Label(master, text="Semester",bg='#FFFFFF').place(x=50, y=112)

        yearOptions = []
        for x in range(2000, 2050):
            yearOptions.append(str(x) + "")

        self.yearComboBox = ttk.Combobox(master, textvariable =self.yearOption, values=yearOptions)
        self.yearComboBox.config(width=10,font="13")
        self.yearComboBox.place(x=160, y=110)
        self.yearComboBox.set(yearOptions[0])
        self.yearComboBox.bind("<<ComboboxSelected>>", self.updadeFileName)
        self.lblCourseCode = Label(master,text="Year",bg='#FFFFFF').place(x=170, y=112)

        self.txtCourseCode = Entry(master, text="Course code", width=15,font="13",state='readonly')
        self.txtCourseCode.place(x=280, y=110)
        self.txtCourseCode.bind("<Key>", self.updadeFileName)
        self.btnReadFile = Button(master, text="Save", width=9,bg='#5AB1C0',fg='#FFFFFF',font="Verdata 10 bold").place(x=430, y=109)


        self.lblFolderName = Label(master,text="Folder Name",bg='#EAEAEA',font="Verdata 9",relief=SUNKEN,width=53).place(x=40, y=150)


        self.label_2 = Label(master, text="Select the folder to save",bg='#66CCCC',font="Verdata 12").place(x=40, y=180)
        self.txtFolder = Entry(master, text="", font="15", width=31)
        self.txtFolder.place(x=40, y=210)
        self.btnBrowse = Button(master, text="Browse...",font="Verdata 10 bold", width=9,borderwidth=2,relief=SOLID).place(x=330, y=207)
        self.btnSave = Button(master, text="Save", width=9,bg='#5AB1C0',fg='#FFFFFF',font="Verdata 10 bold").place(x=430, y=207)


        self.btnGenerate = Button(master, text="Generate", width=54,bg='#39369C',fg='#FFFFFF',font="Verdata 12", state=DISABLED)
        self.btnGenerate.place(x=30, y=260)

        #Panel "Folder structure"

        #Tree
        self.frame_tree = Frame(height=320, width=500, bd=2, relief='groove').place(x=30, y=305)
        self.viewTree = ttk.Treeview(frame_tree)
        self.viewTree.place(x=50, y=320)
    
        #Panel Instructions

        self.folder_image = ImageTk.PhotoImage(Image.open("./Folder1.png"))
        self.my_label = Label(image=folder_image).place(x=580, y=30)

        self.frmFileName = Frame(height=392, width=240,bd=3, relief='groove',background='#66CCCC').place(x=550, y=230)
        self.folder_image1 = ImageTk.PhotoImage(Image.open("./Description.png"))
        self.my_label1 = Label(image=folder_image1).place(x=560, y=270)

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