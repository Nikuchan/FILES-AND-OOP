#File Objects
#Normal way of Using Files
#f= open('test.txt')

#print(f.name)
#print(f.mode)

#f.close()

#print(f.closed)

print("Using Context Managers to access files")


with open('test.txt','r') as f:
    #f_contents=f.read()
    #f_contents = f.readlines()
    '''
    for line in f:
        print(line,end='')'''
    size_to_read=10
    f_contents=f.read(size_to_read)
    while len(f_contents)>0:
        print(f_contents,end='')
        f_contents=f.read(size_to_read)

    print("\nChecking out how seek and tell works")
    print(f.tell())
    f.seek(0)
    print(f.tell())



    '''f_contents = f.readline()
    print(f_contents,end='')

    f_contents = f.readline()
    print(f_contents,end='')'''







