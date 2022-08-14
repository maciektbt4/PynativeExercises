def checkIfFileIsEmpty(fileName):
    with open (fileName, "r") as fp:
        if len(fp.readlines()) == 0:
            return "File is empty as hell!"
        else:
            return "You can dig in, smth is there!!!"

print(checkIfFileIsEmpty("empty.txt"))
print(checkIfFileIsEmpty("output_file.txt"))