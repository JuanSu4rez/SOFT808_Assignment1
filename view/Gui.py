from Tkinter import *
import tkFileDialog
from tkinter import PhotoImage
import ttk
import tkMessageBox

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
        self.frmUploadFile = Frame(height=60, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=10)
        self.lblLoadFile = Label(master, text="1. Upload a Word file", bg='#66CCCC', font="Verdata 12").place(x=15, y=0)

        self.txtFilePath = Entry(master, text="", width=100)
        self.txtFilePath.place(x=15, y=30)

        self.uploadIcon = PhotoImage(file="./uploadIcon.gif")
        self.btnUploadFile = Button(master, text="Browse...", image=self.uploadIcon, fg='#990000', font="Verdata 10 bold", width=60, height=26, command=self.uploadFile).place(x=625, y=25)
        #self.btnReadFile = Button(master, text="Read file", bg='#DB0000', fg='#FFFFFF', font="Verdata 10 bold", width=8, command=self.readFile).place(x=310, y=60)

        #Panel "Setting values"
        self.frmFileName = Frame(height=180, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=80)
        self.lblPnlSettingValues = Label(master, text="2. Setting values", fg='#990000', bg='#66CCCC', font="Verdata 12 bold").place(x=15, y=70)
        self.lblSemester = Label(master, text="Semester - Year", bg='#66CCCC', font="Verdata 11").place(x=15, y=100)

        semesterOptions = ["S1", "S2", "S3"]

        yearOptions = []
        for x in range(2000, 2050):
            for y in semesterOptions:
                yearOptions.append(y + "-" + str(x))

        self.semesterComboBox = ttk.Combobox(master, textvariable =self.semesterOption, values=yearOptions)
        self.semesterComboBox.config(width=12)
        self.semesterComboBox.place(x=15, y=130)
        self.semesterComboBox.set(yearOptions[0])
        self.semesterComboBox.bind("<<ComboboxSelected>>", self.updadeFileName)

        #self.lblYear = Label(master, text="Year", bg='#66CCCC', font="Verdata 11").place(x=100, y=120)

        #yearOptions = []
        #for x in range(2000, 2050):
        #    yearOptions.append(str(x) + "-" + semesterOptions[x%semesterOptions.__len__()])

        #self.yearComboBox = ttk.Combobox(master, textvariable =self.yearOption, values=yearOptions)
        #self.yearComboBox.config(width=8)
        #self.yearComboBox.place(x=100, y=150)
        #self.yearComboBox.set(yearOptions[0])
        #self.yearComboBox.bind("<<ComboboxSelected>>", self.updadeFileName)

        self.lblCourseCode = Label(master, text="Course code", bg='#66CCCC', font="Verdata 11").place(x=135, y=100)

        self.txtCourseCode = Entry(master, text="", width=12, state='readonly')
        self.txtCourseCode.place(x=135, y=130)
        self.txtCourseCode.bind("<Key>", self.updadeFileName)

        self.lblFolderName = Label(master, text="Folder name", bg='#66CCCC', font="Verdata 11").place(x=240, y=100)

        self.txtFolderName = Entry(master, text="", width=75, state='readonly')
        self.txtFolderName.place(x=240, y=130)

        self.lblDestination = Label(master, text="Select folder destination", bg='#66CCCC', font="Verdata 11").place(x=15, y=160)

        self.txtFolderPath = Entry(master, text="", width=100)
        self.txtFolderPath.place(x=15, y=190)

        self.destinationFolderIcon = PhotoImage(file="./destinationIcon.gif")
        self.btnSelectDestination = Button(master, text="Browse...",  image=self.destinationFolderIcon, borderwidth=2, relief=SOLID, font="Verdata 10 bold", width=60, height=26, command=self.selectDestination)
        self.btnSelectDestination.place(x=625, y=185)

        self.btnGenerate = Button(master, text="Generate", bg='#39369C', fg='#FFFFFF', font="Verdata 12", width=8, state=DISABLED, command=self.generate)
        self.btnGenerate.place(x=310, y=220)

        #Panel "Folder structure"

        #Tree
        self.frmTree = Frame(height=300, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=270)
        self.lblFolderStructure = Label(master, text="Folder structure", bg='#66CCCC', font="Verdata 11").place(x=15, y=260)
        self.treeView = ttk.Treeview(master, height=12)
        self.treeView.place(x=10, y=290)

        vsb = ttk.Scrollbar( orient="vertical", command=self.treeView.yview)
        vsb.place(x=681, y=292, height=264)

        self.treeView.configure(yscrollcommand=vsb.set)

        self.treeView["columns"] = ("one")
        self.treeView.column("#0", width=486, minwidth=486, stretch=NO)
        #self.treeView.column("one", width=200, minwidth=150, stretch=NO)
        #self.treeView.column("two", width=185, minwidth=150, stretch=NO)


        #self.treeView.heading("#0", text="")
        #self.treeView.heading("one", text="")
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

        self.imgFolder = PhotoImage(file="Folder.gif")
        self.imgFile = PhotoImage(file="File.gif")

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

    def drawTree(self, folderName, arrayFolders):
        tree = self.treeView

        #tree["columns"] = ("one")
        #tree.column("#0", width=285, minwidth=270, stretch=NO)
        #tree.column("one", width=150, minwidth=150, stretch=NO)

        tree.heading("#0", text="- Name -")
        #tree.heading("one", text="- Date modified -")

        stage_1 = ["Assessment", "ClassRoll", "CourseOutline", "CourseResultSummary", "LectureMaterial", "Other Documents", "SpreadSheet"]
        courseOutline = ["Drafts", "ModerationForm"]
        lectureMaterial = ["Book", "Week1", "Week2", "Week3", "Week4", "Week5", "Week7", "Week8", "Week9", "Week10", "Week11", "Week12"]
        moderationMaterial = ["ModerationForms", "ThreeSamples"]

        mainFolder = tree.insert("", 1, folderName, text=folderName, image=self.imgFolder)      # Main folder
        iterator = 0

        for x in stage_1:
            tree.insert(mainFolder, iterator, x, text=x,  image=self.imgFolder)
            iterator = iterator+1

        iterator = 0
        for x in arrayFolders:
            tree.insert("Assessment", 1, x, text=x, image=self.imgFolder)
            tree.bind("<Double-1>", self.OnDoubleClick)
            tree.insert(x, iterator, text="Drafts", image=self.imgFolder)
            if iterator == 0:
                tree.insert(x, iterator, iid="Child1", text="ModerationMaterial", image=self.imgFolder)
                #tree.insert(x, iterator, text="ModerationMaterial", image=self.imgFolder)
            else:
                tree.insert(x, iterator, text="ModerationMaterial", image=self.imgFolder)
            tree.insert(x, iterator, text="Submissions", image=self.imgFolder)
            iterator = iterator + 1

        for x in moderationMaterial:
            tree.insert("Child1", 1, x, text=x, image=self.imgFolder)

        for x in courseOutline:
            tree.insert("CourseOutline", 2, x, text=x, image=self.imgFolder)

        tree.insert("Drafts", 2, "Soft808", text="Soft808", image=self.imgFile)
        tree.insert("Drafts", 2, "Soft808_2", text="Soft808_2", image=self.imgFile)

        for x in lectureMaterial:
            tree.insert("LectureMaterial", 2, x, text=x, image=self.imgFolder)

    def OnDoubleClick(self, event):
        item = self.treeView.identify('item', event.x, event.y)
        print("you clicked on", self.treeView.item(item, "text"))
        self.showMessage("click", "click me")

    def uploadFile(self):
        print "upload file GUI"
        pathSelectedFile = tkFileDialog.askopenfile(title="Select a Word file", filetypes=[('Word file', '*.docx'), ('Word file', '*.doc')])
        if pathSelectedFile is not None:
            self.myController.uploadFile(pathSelectedFile.name)

    def readFile(self):
        self.myController.readFile()

    def showError(self, errorTitle, errorDescription):
        tkMessageBox.showerror(errorTitle, errorDescription)

    def showMessage(self, title, description):
       tkMessageBox.showinfo(title, description)

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
