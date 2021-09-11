import random

print("Rules of the game as follows: \n"
       "Rock vs paper->paper wins \n"
       "Rock vs scissor->Rock wins \n"
       "paper vs scissor->scissor wins \n")
count = 0
user = 0
comp = 0
dicts = {}

def rules(a,b):
    a = choice
    b = comp_choice
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

    return result

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


    print(f"user choice is: {choice_name} " )
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

    print(f"Computer choice is: {comp_choice_name} ")

    print(choice_name + " V/s " + comp_choice_name)


    result = rules(choice,comp_choice)

    if result == choice_name:
        print(" User wins ")
        a = "user"
        user += 1
    else:
        print(" Computer wins ")
        a = "computer"
        comp +=  1

    dicts[0 + count] = [choice_name, comp_choice_name, a]
    #print(dicts)

    count = count + 1


print(f"\nPoints by user : {user} \nPoints by computer : {comp}" )

if user > comp:
    print("User wins overall")

elif comp > user:
    print("computer wins overall ")

else:
    print("Game ended TIE")

f='y'
while(f=='y'):
    try :
        m = int(input("Enter the round for which you need the information :"))

        print(f"Player Choice is {dicts[m-1][0]}" )
        print(f"Computer Choice is {dicts[m-1][1]}")
        print(f"{dicts[m-1][2]} has won round {m}", )
    except:
        print("The round number doesn't exist")
    f = input("Do you want to continue (y/n)")


print("\nThanks for playing")
