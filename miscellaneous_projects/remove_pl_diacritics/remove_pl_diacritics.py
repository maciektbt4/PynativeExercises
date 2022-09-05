import os
import re

dict_pl_diacritics = {"¹": "ą", "ê": "ę", "æ": "ć", "³": "ł", "œ": "ś", "Ÿ": "ź", "¯":"Ż", "¿": "ż"}
files_types = ["txt", "src"]

print(os.getcwd())

files = os.listdir()
print(files)


for file in files:
    # for type in files_types:
    txt_type = False
    for type in files_types:
        if file.__contains__(type):
            txt_type = True
    
    if txt_type == False:
        files.remove(file)

print(files)

for file in files:

    SOURCE_FILE_PATH = file
    DEST_FILE_PATH = file
    source_txt = ""
    dest_txt = []
    with open(SOURCE_FILE_PATH, "r") as fp:
        source_txt = fp.readlines()
        dict_keys = dict_pl_diacritics.keys()    
        for line in source_txt:
            new_line = ""
            for char in line:
                if char in dict_keys:
                    new_line += dict_pl_diacritics[char]
                else:
                    new_line += char
            dest_txt.append(new_line)

    with open(DEST_FILE_PATH, "w") as fp:
        fp.writelines(dest_txt)