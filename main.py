from random import choice

lists =["Rock","Paper","Scissors"]
done = False
while not done:
    choice_made = None
    CPU = choice(lists)
    user_input = input("\n Enter R for Rock, P for Paper, S for Scissors :\n")
    
    if user_input == 'R':
        user_chioce = "Rock"
        choice_made = 'valid'
    elif user_input == 'S':
        user_chioce = "Scissors"
        choice_made = 'valid'
    elif user_input == 'P':
        user_chioce = "Paper"
        choice_made = 'valid'
    else:
        print("Not valid try again")
    if choice_made == 'valid':
        print(f"The computer selected {CPU} while you selected {user_chioce}")
        if user_chioce == CPU:
            print("It is a tie")
        else:
            if user_chioce == 'Rock':
                if CPU =='Paper':
                    print("Machine Wins")
                else:
                    print ("You win")
            if user_chioce == 'Paper':
                if CPU =='Scissors':
                    print("Machine Wins")
                else:
                    print ("You win")
            if user_chioce == 'Scissors':
                if CPU =='Rock':
                    print("Machine Wins")
                else:
                    print ("You win")
            done = True

    
        

