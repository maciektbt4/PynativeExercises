def removeChars(string, n):

    print(f"Original string:\n {string}")

    return string[n:]

longString = input("write string: ")
n = int(input("How many characters do you want to remove?: "))

print("New string:\n " + removeChars(longString, n))