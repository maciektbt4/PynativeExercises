"""
This is class which contain all necessary methods to change names.

It check corectness of files in source path rename it to proper
names and save them in destination path.
"""

import os
import re

class ManageFiles:
    """Class representing a file managment."""

    def __init__(self, source_path, destination_path) -> None:
        """
        Set up source and destination path.

        Args:
            source_path: Path to files to change.
            destination_path: Path where files with changed name should be saved
        """
        self.source_path = source_path
        self.destination_path = destination_path

    def change_current_dir(self):
        """Change current location to defined in source path."""
        os.chdir(self.source_path)

    def print_current_dir(self):
        """Print current location path."""
        print(os.getcwd())

    def list_folder_elements(self):
        """List files in current location and return them in list."""
        print(os.listdir())
        return os.listdir()

    def create_test_files(self, num = 10):
        """Create testing files. By default 10 files are created."""
        for i in range(1, num):
            filename = str(i) + ".py"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(f"That's file name named {filename}")

    def find_files_with_wrong_names(self, files_list):
        """Check which files have incorrect names."""
        # Define regex pattern to find only wrong names - names with 1 decimal and .py end
        regex_pattern = r"\d.py"
        matches = []
        for file in files_list:
            # Check if regex pattern is matched and return value is not none
            if re.match(regex_pattern, file) is not None:
                matched_object = re.match(regex_pattern, file)
                # Append only values from matched object returned from re.match
                matches.append(matched_object.group(0))
        return matches

    def rename_files_with_correct_names(self, files):
        """Correct names.

        Add '0' on the begining of file - eg. '1.py' is changing to '01.py'
        """
        for file in files:
            corrected_name = "0" + file
            os.replace(file, corrected_name)

    def remove_files(self, *folder_path):
        """Remove testing files (all from current location)."""
        for file in folder_path:
            file_path = self.source_path + str(r"/" + file)
            os.remove(file_path)
