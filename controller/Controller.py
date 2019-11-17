from model import Model as myModel
from view import Gui as myGui
from Tkinter import *

#   SOFT808 Software User Experience
#   Juan Sebastian Suarez
#   controller - Controller

class Controller:
    strFolderName = None

    def __init__(self):
        # print "constructor control"
        self.model = myModel.Model()
        self.gui = myGui.Gui(master=root)
        self.gui.setController(self)

        self.gui.mainloop()

    def readFile(self):
        #print "readFile controller"
        pathFileToRead = self.gui.txtFilePath.get()
        self.model.readFile(pathFileToRead)
        self.updateCourseCode()
        #self.updadeFolderNameToGenerate()
        #self.gui.drawTree(self.strFolderName, self.model.arrayFolders)


    def updateCourseCode(self):
        self.gui.txtCourseCode["state"] = 'normal'
        #self.gui.txtCourseCode.delete(0, END)
        #self.gui.txtCourseCode.insert(0, self.model.extractedCourseCode)
        self.gui.txtCourseCode["text"] = self.model.extractedCourseCode
        #self.gui.txtCourseCode["state"] = 'readonly'
        #print "COntroller updateCourseCode"

    def uploadFile(self, param):
        pathFileToRead = param
        self.gui.txtFilePath.delete(0, END)
        self.gui.txtFilePath.insert(0, pathFileToRead)
        self.gui.resetValues()
        try:
            self.readFile()
            self.gui.showMessage("Success !","The file was read successfully")
            self.gui.activateBtnNext()
            self.gui.activateTabStep2()
        except IndexError as e:
            self.gui.showError("Error !", "The file does not have the correct structure")
            print str(e)
            print str(e.__class__)
            self.gui.txtFilePath.delete(0, END)
            self.gui.txtFilePath.insert(0, "")
            self.gui.deactivateBtnNext()
            self.gui.disableTabStep2()


    def updateFolderDestination(self):
        pathDestination = self.gui.strPathSelectedFolder
        if pathDestination.__class__ == unicode:
            self.gui.setPathDestination(pathDestination)
            if self.gui.semesterComboBox.current() != 0:
                self.gui.activateBtnGenerate()

    def updadeFolderNameToGenerate(self):
        # self.strFolderName = self.gui.semesterComboBox.get() + "-" + self.gui.yearComboBox.get() + "-" + self.gui.txtCourseCode.get()
        if self.gui.semesterComboBox.current() != 0:
            #self.strFolderName = self.gui.semesterComboBox.get() + "-" + self.gui.txtCourseCode.get()
            self.strFolderName = self.gui.semesterComboBox.get() + "-" + self.gui.txtCourseCode["text"]
            self.gui.txtFolderName["state"] = 'normal'
            self.gui.txtFolderName["text"] = self.strFolderName
            #self.gui.txtFolderName.insert(0, self.strFolderName)
            #self.gui.txtFolderName["state"] = 'readonly'
            pathDestination = self.gui.strPathSelectedFolder
            self.gui.drawTree(self.strFolderName, self.model.arrayFolders)
            if len(pathDestination) > 0:
                self.gui.activateBtnGenerate()
            print "path destination [" +  pathDestination + "]"
        #print "Controller updadeFolderNameToGenerate"


    def generateFolders(self):
        #print "generateFolders() Controller"
        # TODO generate the name of the folder
        # self.model.createFolders(self.gui.strFolderName, self.gui.strPathSelectedFolder)
        try:
            self.model.createFolders(self.strFolderName, self.gui.strPathSelectedFolder)
            #self.gui.showMessage("Success !", "The folders have been generated")
            self.gui.showSuccesDialog("Success !", "The folders have been generated" + "\n\n" + "Would you like to open the destination folder ?", self.gui.strPathSelectedFolder + "/" + self.strFolderName)
        except Exception as e:
            self.gui.showError("Error !", "There was an error during the folder generation" + "\n\n" + str(e))


if __name__ == '__main__':
    root = Tk()
    control = Controller()

# model = myModel.Model()
# app = myGui.Gui(master=root)
# app.mainloop()


# main = Tk()
# main.title("SOFT808 UX")
# main.geometry("900x600")
# app = MainApp(main)
# main.mainloop()
