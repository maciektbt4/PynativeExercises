def stringBalanceTest(string1, string2):
    for s in string1:
        if str(string2).count(s) == 0:
            return False
    return True


s1 = "Yn"
s2 = "PYnative"
print("String are balanced" if stringBalanceTest(s1, s2) else "Strings are not balanced")

s3 = "Ynf"
s4 = "PYnative"
print("String are balanced" if stringBalanceTest(s3, s4) else "Strings are not balanced")