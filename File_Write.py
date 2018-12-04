with open('test2.txt','w') as f:
    f.write("Test")
    f.seek(0)
    f.write("R") # This is going to overwrite the 'T' in Test in the file
