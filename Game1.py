import random
print("This Is Snake,Water,Gun")
s1 = ["snake", "water", "gun"]
computer = random.choice(s1)
# print(computer)
int = input("tell me your input\n")
if computer=='snake' and int=='water':
    print("You've Won")
elif computer=='snake' and int=='gun':
    print("You've won")
elif computer=='water' and int=='snake':
    print("You've lost")
elif computer=='water' and int=='gun':
    print("You've Lost")
elif computer=='gun' and int=='water':
    print("you've won")
elif computer=='gun' and int=='snake':
    print("You've lost")

else:
    print("Try again The match is Draw")