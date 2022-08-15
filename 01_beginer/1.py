prevNumber = 0
for i in range(10):
    print("Current Number %s Previous Number  %s  Sum:  %s" % (i, prevNumber, i + prevNumber))
    prevNumber = i