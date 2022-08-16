# 1A
str1 = "James"
print("Original string is ", str1)
print("Every second letter of this string is ", str1[::2])

middleCharInString = str1[int(len(str1)/2)]
resultString = str1[0] + middleCharInString + str1[-1]

print("First, midle and end string result is ", resultString)