import docx
import os
import docx2txt
from shutil import copyfile


#   SOFT808 Software User Experience
#   Juan Sebastian Suarez
#   model - Model

class Model:

    cdPath=""
    pathSelectedFile = ""
    nameSelectedFile = ""
    extractedCourseCode = ""
    arrayFolders = []


    def __init__(self):
        print "constructor model"

    def chooseFile(self):
        print "chooseFile"

    def refreshFileName(self):
        print "refreshFileName "

    def enableBtnProcess(self):
        self.btnProcess["state"] = "active"

    def readFile(self, pathFile):
        #print "readFile model " + pathFile
        text = docx2txt.process(pathFile)
        self.cdPath = pathFile
        #Course Code
        indexOneCode = text.find("Course Code")
        indexTwoCode = text.find("Course Title")
        courseCodeText = text[indexOneCode:indexTwoCode].split('\n\n')
        self.extractedCourseCode = str(courseCodeText[1])

        #print self.extractedCourseCode

        #Folder structure
        indexOne = text.find('Summative Assessment')
        indexTwo = text.find('Content')
        #splitResult = text[indexOne:indexTwo].split('\n')
        splitResult = text[indexOne:indexTwo].split('\n\n\n')
        #print text[indexOne:indexTwo]
        #for i in splitResult:
            #print "[" + i + "]"

        secondResult = {}

        for x in range(1, len(splitResult)):
            #print "{" + splitResult[x] + "}"
            secondResult[x-1] = splitResult[x].split('\n')
            #print x

        self.arrayFolders = []
        for j in secondResult:
            if secondResult[j][1] is not None:
                print secondResult[j][1]
                #self.arrayFolders.append(str(secondResult[j][1]))
                self.arrayFolders.append((str(secondResult[j][1])).strip())
            else:
                print "empty row"

        #for p in self.arrayFolders:
        #    print p

##############################################################################
##############################################################################

    def createFolders(self, folderName, pathDestination):
        #print " - createFolders model - "
        #  print "The folders should be created in " + str(pathDestination) + " with the name " + str(folderName)
        backslash = "/"
        main_folder = pathDestination + backslash + folderName

        os.mkdir(main_folder)

        stage_1 = ["Assessment", "ClassRoll", "CourseOutline", "CourseResultSummary", "LectureMaterial", "Other Documents", "SpreadSheet"]

        assesment = self.arrayFolders
        print "\n Model_CreateFolders \n"
        print assesment
        courseOutline = ["Drafts", "ModerationForm"]
        lectureMaterial = ["Book", "Week1", "Week2", "Week3", "Week4", "Week5", "Week7", "Week8", "Week9", "Week10", "Week11", "Week12"]


        drafts = "Soft808.docx"

        moderationMaterial = ["ModerationForms", "ThreeSamples"]
        backslash = "/"

        for w in stage_1:
            os.mkdir(main_folder + backslash + w)

        for x1 in assesment:
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1)
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1 + backslash + "Drafts")
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1 + backslash + "ModerationMaterial")
            os.mkdir(main_folder + backslash + "Assessment" + backslash + x1 + backslash + "Submissions")

        for x2 in courseOutline:
            os.mkdir(main_folder + backslash + "CourseOutline" + backslash + x2)

            week6 = "Week6"
        for x3 in lectureMaterial:
            os.mkdir(main_folder + backslash + "LectureMaterial" + backslash + x3)
        os.mkdir(main_folder + backslash + "LectureMaterial" + backslash + week6)

        #print "source " + self.cdPath
        #print "destination " + main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + drafts
        #print "drafts " + drafts

        destinationFolder = self.cdPath.split('/')

        #print "------------------------------"
        #print destinationFolder

        copyfile(self.cdPath, main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + destinationFolder[len(destinationFolder) - 1])

        newDoc = docx.Document()
        newDoc.add_paragraph("Sample Course Outline")
        newDoc.save(main_folder + backslash + "CourseOutline" + backslash + "Drafts" + backslash + drafts)

        for z in moderationMaterial:
            for y in self.arrayFolders:
                os.mkdir(
                    main_folder + backslash + "Assessment" + backslash + y + backslash + "ModerationMaterial" + backslash + z)

    def getExtractedCourseCode(self):
        return self.extractedCourseCode
