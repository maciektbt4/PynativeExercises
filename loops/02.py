for rows in range(1,6):
    
    outputPattern = ""
    
    for columns in range(1, rows + 1):
        outputPattern += str(columns) + " "
        
    print(outputPattern)