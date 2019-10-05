from model import Model as myModel
from view import Gui as myGui
from Tkinter import *

class Controller:

    def __init__(self):
        print "constructor control"
        self.model = myModel.Model()
        self.gui = myGui.Gui(master=root)
        self.gui.setController(self)
        #gui events

        #self.gui.btnUploadFile.bind("<Button>", self.uploadFile)
        #self.gui.btnSelectDestination.bind("<Button>", self.updateFolderDestination)
        #self.gui.btnSelectDestination.bind("<Button>", self.updateFolderDestination)

        self.gui.drawTree()
        self.gui.mainloop()


    def readFile(self, event):
        print "readFile controller"
        self.model.readFile()

    def uploadFile(self, event):
        print "refreshUploadedFile"
        self.gui.updatePathloadedFile(self.gui.pathSelectedFile)

    def updateFolderDestination(self):
        pathDestination = self.gui.strPathSelectedFolder
        if pathDestination.__class__ == unicode:
            self.gui.setPathDestination(pathDestination)
            self.gui.enablebtnGenerate()

    def generateFolders(self):
        print "generateFolders() Controller"
        #TODO generate the name of the folder
        #self.model.createFolders(self.gui.strFolderName, self.gui.strPathSelectedFolder)
        self.model.createFolders("F O L D E R N A M E", self.gui.strPathSelectedFolder)



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