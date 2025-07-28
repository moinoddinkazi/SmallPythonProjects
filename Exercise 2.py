print("What Do you want to calculate")

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second Number\n"))
num3 = input("Which one you want+,-,/,*\n")
if num1==45 and num2==3 and num3=='*' :
    print("Ans Is 555")
elif num1==56 and num2==9 and num3=='+' :
    print("Ans Is 77")
elif num1==56 and num2==7 and num3=='/' :
    print("Ans Is 4")
elif num3=='*':
    multi=num1+num2
    print(multi)
elif num3 == '+':
    add=num1+num2
    print(add)
elif num3=='-':
    sub=num1-num2
    print(sub)
elif num3=='/' :
    div=num1/num2
    print(div)
else:
    print("Thanks Alot")

