

no_of_guesess = 1
print("No of guesses are only 9")
while(no_of_guesess<=9):
    inputed_no=int(input("Guess A number\n"))
    if (inputed_no>15):
        print("Please decrease a no \n")
    elif inputed_no<15:
        print("Tell him to Increase")
    elif(inputed_no==15):
        print("Tell him You Won and Number is 15")

        no_of_guesess = no_of_guesess + 1


    else:


        print("You have Won")
        print(no_of_guesess,"No of guesses you used")

        break

    print("No of guesses left",9 - no_of_guesess)
    no_of_guesess = no_of_guesess + 1

if (no_of_guesess>=9):
    print("You used all Guesses")






