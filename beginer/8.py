#Solution 1:
"""
def checkIfPalindromNumber(number):
    i = len(str(number))

    charlist = []

    for char in number:
        charlist.append(char)

    i = len(charlist)
    for char in charlist:
        if char != number[i-1]:
            return False
        i -= 1
        if i <= len(charlist)/2:
          break
    return True

isPalind = checkIfPalindromNumber(str(76541567))

if isPalind:
    print("Number is palind")
else:
    print("Number is not palind")
"""
# Solution 2:
"""
def revertString(number):
    revertedString = []
    resultString = ""

    for char in number:
        revertedString.insert(0, char)


    for char in revertedString:
        resultString += char
    return resultString

string = str(input("Give me a number: "))
revertString = revertString(string)

print(f"Is {string} equal to {revertString} ? ", end=" Result: ")
if string == revertString:
    print("YES!")
else:
    print("NO!")
"""
# Solution 3:
def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")

palindrome(121)
palindrome(125)