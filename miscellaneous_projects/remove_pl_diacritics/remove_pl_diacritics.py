import os
import re

dict_pl_diacritics = {"¹": "ą", "ê": "ę", "æ": "ć", "³": "ł", "£": "Ł", "ñ": "ń", "œ": "ś", "Ÿ": "ź", "¯":"Ż", "¿": "ż"}
files_types = ["txt", "srt"]

print(os.getcwd())

files = os.listdir()

files=[
    'folder.jpg', 
    'House.of.the.Dragon.S01E01.1080p.HMAX.WEB-DL.DDP5.1.Atmos.x264-CMRG.srt', 
    'house.of.the.dragon.s01e02.1080p.web.h264-cakes[eztv.re].mkv',
    'house.of.the.dragon.s01e02.1080p.web.h264-cakes[eztv.re].srt', 
    'house.of.the.dragon.s01e03.1080p.web.h264-cakes[eztv.re].mkv', 
    'house.of.the.dragon.s01e03.1080p.web.h264-cakes[eztv.re].srt',
    'House.of.the.Dragon.S01E04.Episode.4.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-SMURF.mkv',
    'House.of.the.Dragon.S01E04.Episode.4.1080p.HMAX.WEB-DL.DDP5.1.Atmos.H.264-SMURF.srt',
    'House.of.the.Dragons.S01E01.The.Heirs.of.the.Dragon.2160p.HMAX.WEBRip.DDP5.1.Atmos.HDR.X.265-EVO[eztv.re].mkv', 
    'remove_pl_diacritic.py']

files_reduced = []

for file in files:
    txt_type = False
    for type in files_types:
        if file.__contains__(type):
            txt_type = True
    
    if txt_type == True:
        files_reduced.append(file)

print(files_reduced)

for file in files_reduced:

    SOURCE_FILE_PATH = file
    DEST_FILE_PATH = file
    source_txt = ""
    dest_txt = []
    with open(SOURCE_FILE_PATH, "r", encoding="utf-8") as fp:
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

    with open(DEST_FILE_PATH, "w", encoding="utf-8") as fp:
        fp.writelines(dest_txt)
