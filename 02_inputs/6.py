from distutils import text_file
from queue import Empty


file_text = []
text = ""
with open("input_file.txt","r") as fp:
    file_text = fp.readlines()
    
file_text.remove(file_text[4])

print(file_text)   

with open("output_file.txt","w") as fp:
    fp.writelines(file_text)