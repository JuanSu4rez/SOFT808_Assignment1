
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
       # print "createFolders model"
      #  print "The folders should be created in " + str(pathDestination) + " with the name " + str(folderName)

       backslash = "/"
       main_folder = pathDestination + backslash + folderName

       os.mkdir(main_folder)

       stage_1 = ["Assessment", "ClassRoll", "CourseOutline", "CourseResultSummary", "LectureMaterial",
                  "Other Documents", "SpreadSheet"]

       assesment = ["Assignment1", "MidTerm", "Assignment2", "Final"]
       courseOutline = ["Drafts", "ModerationForm"]
       lectureMaterial = ["Book", "Week1", "Week2", "Week3", "Week4", "Week5", "Week7", "Week8", "Week9", "Week10",
                          "Week11", "Week12"]

       assignment1 = ["Drafts", "ModerationMaterial", "Submissions"]
       midTerm = ["Drafts", "ModerationMaterial", "Submissions"]
       assignment2 = ["Drafts", "ModerationMaterial", "Submissions"]
       final = ["Drafts", "ModerationMaterial", "Submissions"]
       drafts = "Soft808.docx"

       moderationMaterial = ["ModerationForms", "ThreeSamples"]
       backslash = "/"
       for w in stage_1:
           os.mkdir(main_folder + backslash + w)

       for x1 in assesment:
           os.mkdir(main_folder + backslash + "Assessment" + backslash + x1)

       for x2 in courseOutline:
           os.mkdir(main_folder + backslash + "CourseOutline" + backslash + x2)

           week6 = "Week6(Mid Semester Week)"
       for x3 in lectureMaterial:
           os.mkdir(main_folder + backslash + "LectureMaterial" + backslash + x3)
       os.mkdir(main_folder + backslash + "LectureMaterial" + backslash + week6)

       for y1 in assignment1:
           os.mkdir(main_folder + backslash + "Assessment" + backslash + "Assignment1" + backslash + y1)

       for y2 in midTerm:
           os.mkdir(main_folder + backslash + "Assessment" + backslash + "MidTerm" + backslash + y2)

       for y3 in assignment2:
           os.mkdir(main_folder + backslash + "Assessment" + backslash + "Assignment2" + backslash + y3)

       for y4 in final:
           os.mkdir(main_folder + backslash + "Assessment" + backslash + "Final" + backslash + y4)

       newDoc = docx.Document()
       newDoc.add_paragraph("Course Outline")
       newDoc.save(main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + drafts)

       for z in moderationMaterial:
           os.mkdir(
               main_folder + backslash + "Assessment" + backslash + "Assignment1" + backslash + "ModerationMaterial" + backslash + z)

    def printing(self):
        print "printing model"
