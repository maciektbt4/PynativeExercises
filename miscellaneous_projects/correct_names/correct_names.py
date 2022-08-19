import os
import re

class ManageFiles:

    def __init__(self, source_path, destination_path) -> None:
        self.source_path = source_path
        self.destination_path = destination_path
    
    def changeCurrentDir(self):
        os.chdir(self.source_path)
    
    def printCurrentDir(self):
        print(os.getcwd())

    def listFolderElements(self):
        print(os.listdir())
        return os.listdir()

    def createTestFiles(self, num = 10):
        for i in range(1, num):
            filename = str(i) + ".py"
            with open(filename, "w") as file:
                file.write(f"That's file name named {filename}")
    
    def findFilesWithWrongNames(self, files_list):
        # Define regex pattern to find only wrong names - names with 1 decimal and .py end
        regex_pattern = r"\d.py"
        matches = []
        for f in files_list:
            # Check if regex pattern is matched and return value is not none
            if re.match(regex_pattern, f) is not None:
                matched_object = re.match(regex_pattern, f)
                # Append only values from matched object returned from re.match
                matches.append(matched_object.group(0))
        return matches

    def renameFilesWithCorrectNames(self, files):
        for file in files:
            corrected_name = "0" + file
            os.replace(file, corrected_name)


    def removeFiles(self, *file):
        for f in file:
            file_path = self.source_path + str(r"/" + f)
            os.remove(file_path)