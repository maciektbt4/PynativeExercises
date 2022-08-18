import re
str1 = 'I am 25 years and 10 months old'
reg_pattern = r"[^\d]"

# solution with find all
# result = re.findall(reg_pattern, str1)
# strResult = ""
# for s in result:
#     strResult += s

# print(result)
# print(strResult)

# solution with replace
str1 = re.sub(reg_pattern, "", str1)
print(str1)