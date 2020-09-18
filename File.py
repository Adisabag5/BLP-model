import os
from State import State

class File:
    def __init__(self, fileName, path, classification, world, creator):
        self.fileName = fileName
        self.path = path
        self.classification = classification
        self.world = world
        self.creator= creator


    def toString(self):
        print("Name:                " + self.fileName)
        print("Path:                " + self.path)
        print("File class:          " + self.classification)
        print("Belong to the world: " + self.world)
        print("Created by:          " + self.creator)


    def addFileToList(self):
        f = open("worlds/" + self.world + "/filesList.txt", "a+")
        f.write(self.fileName + "," + self.path + "," + self.classification + "," + self.creator  + ","  "\n")


    def getFileData(self, currentState, fileName):
        fileInfo = []
        foundFile = "false"
        x = ""
        with open("worlds/" + currentState.world + "/filesList.txt", 'r') as f:
            for line in f:
                if foundFile == "false":
                    for word in line.split(','):
                        if word == fileName:
                            x = line
                            foundFile = "true"
                            break;
                else:
                    break;
        for word in x.split(','):
            fileInfo.append(word)
        return fileInfo


    def findFile(self, fileName, world):
        dir_path = os.path.dirname(os.path.realpath("worlds/" + world))

        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(fileName + ".txt"):
                    root + '/' + str(file)
                    return "true"
        return "false"



    def convertToInt(self, classification):
        value = 4
        if classification == "Top-secret":
            value = 1
        else:
            if classification == "Secret":
                value = 2
            else:
                if classification == "Confidential":
                    value = 3
                else:
                    if classification == "Unclassified":
                        value = 4
        return value



    def create_file(self, currentState):
        classification = {
            "1": "Top-secret",
            "2": "Secret",
            "3": "Confidential",
            "4": "Unclassified"
        }

        currentClassValue = currentState.classificationValue
        currUser = currentState.userName
        currWorld = currentState.world
        print("Choose the name of the file:")
        fileName = input("Enter your choice")
        print("Choose the file classification:")

        fileClass = "Invalid choice"
        while (fileClass == "Invalid choice"):
            print("1. Top-secret 2. Secret 3. Confidential 4. Unclassified")
            userChoice = input("Enter your choice")
            fileClass = classification.get(userChoice, "Invalid choice")
            if int(userChoice) < currentClassValue:
                fileClass = "Invalid choice"
                print("Your class is too low for that action, please choose a different classification.")
            else:
                f = open("worlds/" + currWorld + "/" + fileName + ".txt", "w")
                path = "worlds/" + currWorld + "/" + fileName + ".txt"
                newFile = File(fileName, path, fileClass, currWorld, currUser)
                newFile.addFileToList()
                f.close()
                print("file created")
                newFile.toString()

    def read_file(self, currentState):
        fileName = input("enter the name of the file:")
        if self.findFile(fileName, currentState.world) == "true" :
            fileData = self.getFileData(currentState, fileName)
            if fileData != ['']:
                if self.convertToInt(fileData[2]) <= self.convertToInt(currentState.classification):
                    f = open(fileData[1], "r")
                    print("---------------------------------")
                    print("  The data was loaded succesfuly")
                    print(f.read())
                    print("---------------------------------")
                else:
                    print("not aloud by the model's rules")
            else:
                print("file not found")



    def write_to_file(self, currentState):
        fileName = input("enter the name of the file:")
        if self.findFile(fileName, currentState.world) == "true":
            fileData = self.getFileData(currentState, fileName)
            if fileData != ['']:
                if self.convertToInt(fileData[2]) <= self.convertToInt( currentState.classification) or self.isAdmin == "true":
                    f = open(fileData[1], "a")
                    newData = input("Write new data to the file:")
                    f.write(newData)
                    print("---------------------------------")
                    print("  The data was added succesfuly")
                    print("---------------------------------")
                else:
                    print("not aloud by the model's rules")
                    print("---------------------------------")

            else:
                print("---------------------------------")
                print("file not found")
                print("---------------------------------")
                return



    def delete_file(self, currentState):
        fileName = input("enter the name of the file:")
        if self.findFile(fileName, currentState.world) == "true":
            fileData = self.getFileData(currentState, fileName)
            print(fileData)
        else:
            print("---------------------------------")
            print("File does not exist")
            print("---------------------------------")
            return
        if self.userName == fileData[3] or self.isAdmin == "true":
            with open("worlds/" + currentState.world + "/filesList.txt", "r") as f:
                lines = f.readlines()
            with open("worlds/" + currentState.world + "/filesList.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != (fileData[0] + "," + fileData[1]+ "," +fileData[2] + "," + fileData[3]+ ","):
                        f.write(line)
            os.remove(fileData[1])
            print("---------------------------------")
            print("file deleted")
            print("---------------------------------")
        else:
            print("---------------------------------")
            print("You are not aloud to delete this file, you are not its creator!")
            print("---------------------------------")