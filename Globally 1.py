l = 5  # Global variable/scope
def  function1(n):
    #l = 15    #uses only in func1 / local
    global l
    l=l+45
    print(l)
    print(n,"welcome to World")
function1("Hey!")