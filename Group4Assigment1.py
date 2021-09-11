import random
"winner"
user_count=0
computer_count=0

winning_options = [(0,2), (1,0), (2,1)]
output_dict={}
for i in range(1,11):
    choice=int(input("\n1.Rock \n2.Paper \n3.Scissors\nEnter your choice :"))

    if(choice==1):
        user_choice="rock"
        print("User Choice is :",user_choice)
    elif(choice==2):
        user_choice="paper"
        print("User Choice is :", user_choice)
    elif(choice==3):
        user_choice="scissors"
        print("User Choice is :", user_choice)
    else:
        print("Invalid Choice")

    computer_choice=random.randint(1, 3)

    if computer_choice == 1:
        computer_choice_name = 'Rock'
    elif computer_choice == 2:
        computer_choice_name = 'paper'
    else:
        computer_choice_name = 'scissor'

    print("Computer Choice is :",computer_choice_name)

    if(choice==computer_choice):
        user_count=user_count+0
        computer_count=computer_count+0
        winner="Nonone"
    elif((choice,computer_choice) in winning_options):
        user_count=user_count+1
        winner="Player"
    else:
        computer_count=computer_count+1
        winner="Computer"
    output_dict[i] = [user_choice, computer_choice_name, winner]
print("Points Earned by Player:",user_count)
print("Points Earned by Computer:",computer_count)
if(user_count==computer_count):
    print("No one is Winner")
elif(user_count>computer_count):
    print("Overall Winner is Player")
else:
    print("Winner is Computer")
choice='y'
while(choice=='y'):
    try:
        round_number = int(input("\nEnter the round for which you need information :\n"))
        print("Player Choice is {}".format(output_dict[round_number][0]))
        print("Computer Choice is {}".format(output_dict[round_number][1]))
        print("{} has won round {}".format(output_dict[round_number][2],round_number))
    except:
        print("The round number doesn't exist")
    choice=input("Do you want to continue (y/n)")

