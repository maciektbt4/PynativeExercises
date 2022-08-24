"""
This is an script for automatic renaming incorrect file names.

It check corectness of files in source path rename it to proper
names and save them in destination path.
"""

from correct_names import ManageFiles

# Ask user to define source and destination paths
# source_path = input("Pass source path: ")
# destination_path = input("Pass destination path: ")

# For test reason we are using fixed paths
SOURCE_PATH = r"/home/maciek/Documents/Python/test"
DESTINATION_PATH = r"/home/maciek/Documents/Python/test"

file_manager = ManageFiles(SOURCE_PATH, DESTINATION_PATH)

# Change current location to source path location
file_manager.change_current_dir()

# Print location path
file_manager.print_current_dir()

# Create 30 test files in current location
file_manager.create_test_files(num=30)

# Save in list files from current location
folder_elements = file_manager.list_folder_elements()

# Check and save in list, files with incorrect names
matches  = file_manager.find_files_with_wrong_names(folder_elements)
print(matches)

# Correct file names 
file_manager.rename_files_with_correct_names(matches)

# Save in list folder elements
folder_elements = file_manager.list_folder_elements()
print(folder_elements)

# Add the end remove all test files
file_manager.remove_files(*folder_elements)
