#x= 'Global x'
print("\nTesting Global and Local Scope")
def test():
    global x #Explicitly telling python that we want to work on Global x Variable
    #y='Local y'
    x='Local x'
    #print(y)
    print(x)
test()
print(x)

m=min([3,4,5,6])
print(m)

print("\nTesting Enclosing Scope")
def outer():
    x='outer x'

    def inner():
        nonlocal x #Explicitly telling python that we want to work with outer function's variable x
        #x='inner x'
        print(x)

    inner()
    print(x)

outer()