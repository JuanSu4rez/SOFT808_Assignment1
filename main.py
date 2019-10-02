from Tkinter import *
import tkFileDialog
from pathlib import Path
import os
import docx2txt


class MainApp:
    pathSelectedFile = ""
    nameSelectedFile = ""
    folderCounter = 0

    def __init__(self, param):
        myFrame = Frame(param)
        myFrame.pack()

        self.lblLoadFile = Label(myFrame, text="Select a Word file")
        self.lblLoadFile.pack()

        self.txtNameFile = Entry(myFrame, text="", width=140)
        self.txtNameFile.pack()

        self.btnUpload = Button(myFrame, text="load file", width=10, command=self.chooseFile)
        self.btnUpload.pack()

        self.btnProcess = Button(myFrame, text="read file", width=10, state=DISABLED, command=self.readFile)
        self.btnProcess.pack()

        self.txtFileContent = Text(myFrame, height=26, width=50)
        self.txtFileContent.pack(side=LEFT)

        scroll = Scrollbar(myFrame, command=self.txtFileContent.yview)
        scroll.pack(side=RIGHT, fill=Y)

        self.txtFileContent.configure(yscrollcommand=scroll.set)

        self.btnCreateFolder = Button(myFrame, text="create fold", width=10, command=self.createFolder)
        #self.btnCreateFolder.pack()

    def chooseFile(self):
        pathFile = tkFileDialog.askopenfile(title = "Select a Word file", filetypes=[('Word file','*.docx')])
        if pathFile is not None:
            self.pathSelectedFile = pathFile.name
            print "Full path "+ self.pathSelectedFile
            self.nameSelectedFile = Path(pathFile.name)
            self.refreshFileName()
            self.enableBtnProcess()
        else:
            print "3 no file was selected"

    def refreshFileName(self):
        self.txtNameFile.delete(0, END)
        self.txtNameFile.insert(0, self.pathSelectedFile)

    def enableBtnProcess(self):
        self.btnProcess["state"] = "active"

    def readFile(self):
        textFromFile = docx2txt.process(self.pathSelectedFile)
        print(textFromFile)
        self.txtFileContent.delete('1.0', END)
        self.txtFileContent.insert(END, textFromFile)

        print "reading the selected file"

    def createFolder(self):
        print "33333333 "
        print  os.path.exists('C:\\PYTHONFOLDERTEST')
        if os.path.exists('C:\\PYTHONFOLDERTEST') == False:
            os.mkdir('C:\\PYTHONFOLDERTEST')
        else:
            self.folderCounter = self.folderCounter + 1
            os.mkdir('C:\\PYTHONFOLDERTEST(' + self.folderCounter.__str__() + ")")

    def printing(self):
        print "printing "


main = Tk()
main.title("SOFT808 UX")
main.geometry("900x600")
app = MainApp(main)
main.mainloop()
