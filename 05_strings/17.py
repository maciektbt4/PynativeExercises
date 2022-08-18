import re
str1 = "35sasa is Data 50dsds and AI Expert"
reg_pattern = r"\w+\d+"

# Not correct solution
# Write words consits of alphanumeric and ending with digits
results = re.findall(reg_pattern, str1)
for s in results:
    print(s)

# Correct solution
# Write full word combined from digits and alphanumeric
splitedString = str1.split(" ")
for s in splitedString:
    if re.match(reg_pattern, s) is not None:
        print(s)