from model import Model as myModel
from view import Gui as myGui
from Tkinter import *

class Controller:

    strFolderName = None

    def __init__(self):
        print "constructor control"
        self.model = myModel.Model()
        self.gui = myGui.Gui(master=root)
        self.gui.setController(self)

        self.gui.drawTree()
        self.gui.mainloop()

    def readFile(self):
        print "readFile controller"
        pathFileToRead =  self.gui.txtFilePath.get()

        self.model.readFile(pathFileToRead)

    def uploadFile(self, param):
        pathFileToRead = param
        self.gui.txtFilePath.delete(0,END)
        self.gui.txtFilePath.insert(0, pathFileToRead)

    def updateFolderDestination(self):
        pathDestination = self.gui.strPathSelectedFolder
        if pathDestination.__class__ == unicode:
            self.gui.setPathDestination(pathDestination)
            self.gui.enablebtnGenerate()

    def updadeFolderNameToGenerate(self):
        self.strFolderName = self.gui.txtSemester.get() + "-" + self.gui.txtYear.get() + "-" + self.gui.txtCourseCode.get()

        self.gui.txtFolderName["state"] = 'normal'
        self.gui.txtFolderName.delete(0, END)
        self.gui.txtFolderName.insert(0, self.strFolderName)
        self.gui.txtFolderName["state"] = 'readonly'

    def generateFolders(self):
        print "generateFolders() Controller"
        #TODO generate the name of the folder
        #self.model.createFolders(self.gui.strFolderName, self.gui.strPathSelectedFolder)
        self.model.createFolders(self.strFolderName, self.gui.strPathSelectedFolder)

root = Tk()
control = Controller()

#model = myModel.Model()
#app = myGui.Gui(master=root)
#app.mainloop()




#main = Tk()
#main.title("SOFT808 UX")
#main.geometry("900x600")
#app = MainApp(main)
#main.mainloop()