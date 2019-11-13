from Tkinter import *
import tkFileDialog
from tkinter import PhotoImage
import ttk
import tkMessageBox
import webbrowser

#   SOFT808 Software User Experience
#   Juan Sebastian Suarez
#   View - Main frame
class Gui(Frame):

    myController = None
    strPathSelectedFile = ""
    semesterOption = None
    yearOption = None

    btnNextStep1originalPos = None
    btnGenerateoriginalPos = None

    def __init__(self, master):
        print "constructor view"
        self.semesterOption = StringVar()
        self.yearOption = StringVar()
        Frame.__init__(self, master)
        self.master.title("Kit creator")
        self.master.configure(background='#66CCCC')
        self.master.geometry("1100x650")
        self.master.resizable(width=None, height=None)

        self.style = ttk.Style()
        self.style.configure('.', background='#66CCCC')
        self.style.configure('TNotebook.Tab', font=('Verdata', '10', 'bold'))
        self.style.configure('rightTab.TNotebook', font=('Verdata', '10', 'bold'), tabposition='ws')
        #font = ('URW Gothic L', '11', 'bold')

        self.tab_parent = ttk.Notebook(master)

        self.tabInstructions = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.tabInstructions, text=" INSTRUCTIONS ")
        self.tab_parent.pack(expand=0, fill='both')

        self.imgInstructions = PhotoImage(file="./Instructions.gif")
        self.lblImgInstructions = Label(self.tabInstructions, image=self.imgInstructions, borderwidth=1)
        self.lblImgInstructions.pack()
        self.lblImgInstructions.place(x=10, y=10)

        self.nextIcon = PhotoImage(file="./nextIcon.gif")
        self.btnNextInstructions = Button(self.tabInstructions, text="Start ", image=self.nextIcon, compound="right", bg='#ff8c00', font="Verdata 12 bold", width=100, height=30, command=self.nextStep)
        self.btnNextInstructions.place(x=450, y=530)

        self.tabStep1 = ttk.Frame(self.tab_parent)
        self.tab_parent.add(self.tabStep1, text=" STEP 1 OF 2 ")
        self.tab_parent.pack(expand=1, fill='both')
        self.tab_parent.select(self.tabStep1)

        #Panel "Upload a Word file"
        #self.frmUploadFile = Frame(tabStep1,  height=60, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=10)
        self.lblStep1 = Label(self.tabStep1, text="Step 1", fg='#990000', bg='#66CCCC', font="Verdata 16 bold").place(x=5, y=5)

        self.lblLoadFile = Label(self.tabStep1, text="Upload a descriptor file", fg='#990000', bg='#66CCCC', font="Verdata 14 bold").place(x=15, y=100)

        self.txtFilePath = Entry(self.tabStep1, text="", width=100)
        self.txtFilePath.place(x=30, y=158, height=25)

        self.uploadIcon = PhotoImage(file="./uploadFileIcon.gif")
        self.btnUploadFile = Button(self.tabStep1, text="Browse...", image=self.uploadIcon, fg='#990000', font="Verdata 10 bold", width=60, height=26, command=self.uploadFile).place(x=640, y=155)

        self.btnNextStep1 = Button(self.tabStep1, text="Next ", image=self.nextIcon, compound="right", bg='#ff8c00', font="Verdata 12 bold", width=100, height=30, command=self.nextStep)
        self.btnNextStep1.place(x=450, y=530)
        self.btnNextStep1originalPos = self.btnNextStep1.place_info()
        self.btnNextStep1.place_forget()

        #self.btnNextStep1.place()

        #self.btnReadFile = Button(master, text="Read file", bg='#DB0000', fg='#FFFFFF', font="Verdata 10 bold", width=8, command=self.readFile).place(x=310, y=60)

        self.tabStep2 = ttk.Frame(self.tab_parent)
        #self.tab_parent.add(self.tabStep2, text="STEP 2 - Set up the destination folder", state="hidden")
        self.tab_parent.add(self.tabStep2, text=" STEP 2 OF 2 ", state="disabled")
        #self.tab_parent.hide(2)

        #Panel "Setting values"
        #self.frmFileName = Frame(height=180, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=80)
        self.lblStep2 = Label(self.tabStep2, text="Step 2", fg='#990000', bg='#66CCCC', font="Verdata 16 bold").place(x=5, y=5)
        self.lblPnlSettingValues = Label(self.tabStep2, text="Setting values", fg='#990000', bg='#66CCCC', font="Verdata 14 bold").place(x=15, y=50)
        self.lblSemester = Label(self.tabStep2, text="Semester - Year", bg='#66CCCC', font="Verdata 11").place(x=15, y=100)

        semesterOptions = ["S1", "S2", "S3"]

        yearOptions = []
        yearOptions.append("- Select one -")
        for x in range(2000, 2050):
            for y in semesterOptions:
                yearOptions.append(y + "-" + str(x))

        self.semesterComboBox = ttk.Combobox(self.tabStep2, textvariable =self.semesterOption, values=yearOptions)
        self.semesterComboBox.config(width=15)
        self.semesterComboBox.place(x=15, y=130, height=25)
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

        self.lblCourseCode = Label(self.tabStep2, text="Course code", bg='#66CCCC', font="Verdata 11").place(x=135, y=100)

        #self.txtCourseCode = Entry(self.tabStep2, text="", width=12, state='readonly')
        self.txtCourseCode = Label(self.tabStep2, text="", width=12,  font="Verdata 10 bold")
        self.txtCourseCode.place(x=135, y=130, height=25)
        self.txtCourseCode.bind("<Key>", self.updadeFileName)

        self.lblFolderName = Label(self.tabStep2, text="Folder name", bg='#66CCCC', font="Verdata 11").place(x=240, y=100)

        self.txtFolderName = Label(self.tabStep2, text="", width=55, font="Verdata 10 bold")
        self.txtFolderName.place(x=250, y=130, height=25)

        self.lblDestination = Label(self.tabStep2, text="Select folder destination", bg='#66CCCC', font="Verdata 11").place(x=15, y=160)

        self.txtFolderPath = Entry(self.tabStep2, text="", width=100)
        self.txtFolderPath.place(x=15, y=190, height=25)

        self.destinationFolderIcon = PhotoImage(file="./destinationFolder.gif")
        self.btnSelectDestination = Button(self.tabStep2, text="Browse...",  image=self.destinationFolderIcon, borderwidth=2, relief=SOLID, font="Verdata 10 bold", width=60, height=26, command=self.selectDestination)
        self.btnSelectDestination.place(x=625, y=185)

        #self.btnGenerate = Button(self.tabStep2, text="Generate", bg='#39369C', fg='#FFFFFF', font="Verdata 12", width=40, command=self.generate)
        self.btnGenerate = Button(self.tabStep2, text="Generate", bg='#ff8c00', font="Verdata 14 bold", width=20, command=self.generate)
        self.btnGenerate.place(x=220, y=240)
        self.btnGenerateoriginalPos = self.btnGenerate.place_info()
        self.btnGenerate.place_forget()


        #Panel "Folder structure"

        #Tree
        self.frmTree = Frame(self.tabStep2, height=300, width=700, bd=3, relief='groove', bg='#66CCCC').place(x=5, y=300)
        self.lblFolderStructure = Label(self.tabStep2, text="Descriptor structure", bg='#66CCCC', font="Verdata 11").place(x=15, y=290)
        self.treeView = ttk.Treeview(self.tabStep2, height=12)
        self.treeView.place(x=10, y=320)

        vsb = ttk.Scrollbar(self.tabStep2, orient="vertical", command=self.treeView.yview)
        vsb.place(x=681, y=322, height=264)

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
        self.lblImgLogo.place(x=930, y=30)

        #GUI attributes
        self.strPathSelectedFile = ""
        self.strPathSelectedFolder = ""
        self.strFolderName = ""

        #TODO - FIX PATHS TO ICON FILES

        self.imgFolder = PhotoImage(file="Folder.gif")
        self.imgFile = PhotoImage(file="File.gif")

        # self.pack()

    def activateTabStep2(self):
        #self.tab_parent.add(self.tabStep2)
        #self.tab_parent.add(self.tabStep2, state ='normal')
        self.tab_parent.tab(2, state="normal")
        #self.tabStep2["state"]="normal"


    def disableTabStep2(self):
        self.tab_parent.hide(1)

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

    def drawTree(self, folderName, arrayFolders):
        print "GUI drawTree params \n"
        print  folderName
        print "\n"
        print arrayFolders

        tree = self.treeView
        self.cleanTreeView()

        #tree["columns"] = ("one")
        #tree.column("#0", width=285, minwidth=270, stretch=NO)
        #tree.column("one", width=150, minwidth=150, stretch=NO)

        tree.heading("#0", text="- Folder structure -")
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
            #tree.bind("<Button-3>", self.OnDoubleClick)
            tree.insert(x, iterator, text="Drafts", image=self.imgFolder)
            if iterator == 0:
                tree.insert(x, iterator, iid="Child1", text="ModerationMaterial", image=self.imgFolder)
                #tree.insert(x, iterator, text="ModerationMaterial", image=self.imgFolder)
            else:
                tree.insert(x, iterator, text="ModerationMaterial", image=self.imgFolder)
            tree.insert(x, iterator, text="Submissions", image=self.imgFolder)
            iterator = iterator + 1

        for y in moderationMaterial:
            tree.insert("Child1", 1, y, text=y, image=self.imgFolder)

        for x in courseOutline:
            tree.insert("CourseOutline", 2, x, text=x, image=self.imgFolder)

        tree.insert("Drafts", 2, "Soft808", text="Soft808", image=self.imgFile)
        tree.insert("Drafts", 2, "Soft808_2", text="Soft808_2", image=self.imgFile)

        for x in lectureMaterial:
            tree.insert("LectureMaterial", 2, x, text=x, image=self.imgFolder)

        tree.item("Assessment", open=True)
        print "GUI drawTree"

    def OnDoubleClick(self, event):
        item = self.treeView.identify('item', event.x, event.y)
        print("you clicked on", self.treeView.item(item, "text"))
        self.showMessage("click", "click me")

    def uploadFile(self):
        print "upload file GUI"
        pathSelectedFile = tkFileDialog.askopenfile(title="Select a Word file", filetypes=[('Word file', '*.docx'), ('Word file', '*.doc')])
        if pathSelectedFile is not None:
            self.myController.uploadFile(pathSelectedFile.name)


    def nextStep(self):
        self.tab_parent.select(self.tab_parent.index("current") + 1)
        #finalMessage = successDialog(self, "asdasd")
        #finalMessage.wait_window()

    def readFile(self):
        self.myController.readFile()

    def showError(self, errorTitle, errorDescription):
        tkMessageBox.showerror(errorTitle, errorDescription)

    def showMessage(self, title, description):
       tkMessageBox.showinfo(title, description)
       #tkMessageBox.showinfo()

    def showSuccesDialog(self, title, description, mainFodlerPath):
       response = tkMessageBox.askyesno(title, description)
       #MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
       if response == True:
           webbrowser.open('file:///' + mainFodlerPath)
       else:
           #tk.messagebox.showinfo('Return', 'You will now return to the application screen')
           self.destroy()

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

    def getPathDestination(self):
        return self.txtFolderPath.get()

    def updadeFileName(self, event):
        self.myController.updadeFolderNameToGenerate()

    def activateBtnNext(self):
        self.btnNextStep1.place(self.btnNextStep1originalPos)

    def deactivateBtnNext(self):
        self.btnNextStep1.place_forget()
        self.tab_parent.hide(2)

    def activateBtnGenerate(self):
        self.btnGenerate.place(self.btnGenerateoriginalPos)

    def deactivateBtnGenerate(self):
        self.btnGenerate.place_forget()

    def resetValues(self):
        self.semesterComboBox.current(0)
        self.txtFolderName['text'] = ""
        self.txtFolderPath.delete(0, END)
        self.cleanTreeView()
        self.deactivateBtnGenerate()

    def cleanTreeView(self):
        tree = self.treeView
        treeChildren = tree.get_children()
        for item in treeChildren:
            tree.detach(item)
            tree.delete(item)

class successDialog(Toplevel):

    def __init__(self, master, folderPath):
        Toplevel.__init__(self)
        self.master = master
        self.geometry("300x120")
        self.title("Success!")
        self.lift()
        self.focus_force()
        self.grab_set()
        self.resizable( width=False, height=FALSE)
        #self.grab_release()

        # add an entry widget
        self.lblResult = Label(self, text="The folders have been created !", font="Verdata 10 ").place(x=20, y=10)
        #self.e1.pack()

        self.btnNextStep1 = Button(self, text="Open folder", fg='#990000', font="Verdata 10 bold", width=10, height=1, command=self.buttonpressed)
        self.btnNextStep1.place(x=40, y=70)

    def buttonpressed(self):
        #self.master.entryvalue = self.e1.get()
        self.exit_popup()

    def exit_popup(self):
        self.destroy()