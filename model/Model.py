
from pathlib import Path
import os
import docx2txt


class Model:

    pathSelectedFile = ""
    nameSelectedFile = ""

    def __init__(self):
        print "constructor model"

    def chooseFile(self):
        print "chooseFile"

    def refreshFileName(self):
        print "refreshFileName "

    def enableBtnProcess(self):
        self.btnProcess["state"] = "active"

    def readFile(self):
        print "readFile model"

    def createFolders(self, folderName, pathDestination):
        print "createFolders model"
        print "The folders should be created in " + str(pathDestination) + " with the name " + str(folderName)

    def printing(self):
        print "printing model"
