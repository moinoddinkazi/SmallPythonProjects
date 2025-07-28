def funct1(a,b,c,d):
    """This is a function to calculate avrage"""
    average = (a+b+c+d)/4
    return  average
print(funct1.__doc__) #to know what it can do
x = funct1(1,2,3,4)
print("Average Is ",x)