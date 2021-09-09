
import random

print("Rules of the game as follows: \n"
       "Rock vs paper->paper wins \n"
       "Rock vs scissor->Rock wins \n"
       "paper vs scissor->scissor wins \n")
count = 0
user = 0
comp = 0
dicts = {}
while count < 10 :

    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")

    choice = int(input("User turn: "))


    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))


    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'


    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")


    comp_choice = random.randint(1, 3)


    while comp_choice == choice:
        comp_choice = random.randint(1, 3)


    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)


    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("paper wins => ", end="")
        result = "paper"

    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins =>", end="")
        result = "Rock"
    else:
        print("scissor wins =>", end="")
        result = "scissor"


    if result == choice_name:
        print("<== User wins ==>")
        a = "user"
        user = user + 1
    else:
        print("<== Computer wins ==>")
        a = "computer"
        comp = comp + 1

    dicts[0 + count] = [choice_name, comp_choice_name, a]
    print(dicts)







    count = count + 1



print("\n")
print("Points by user : " + str(user))
print("Points by computer : " + str(comp))


if user > comp:
    print("User wins overall")

elif comp > user:
    print("computer wins overall ")

else:
    print("game ended TIE")

m = int(input("Enter the round for which you need the information :"))
print(dicts[m-1])

print("\nThanks for playing")
