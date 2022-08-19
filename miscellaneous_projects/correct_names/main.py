from correct_names import ManageFiles

# source_path = input("Pass source path: ")
# destination_path = input("Pass destination path: ")
source_path = r"/home/maciek/Documents/Python/test"
destination_path = r"/home/maciek/Documents/Python/test"

file_manager = ManageFiles(source_path, destination_path)

file_manager.changeCurrentDir()
file_manager.printCurrentDir()
file_manager.createTestFiles(num=30)

folder_elements = file_manager.listFolderElements()
matches  = file_manager.findFilesWithWrongNames(folder_elements)
print(matches)

file_manager.renameFilesWithCorrectNames(matches)
folder_elements = file_manager.listFolderElements()

file_manager.removeFiles(*folder_elements)