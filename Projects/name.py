import random # Calls random variable generator

games = 0 #Game count variable
while True: #While Loop

    comp =random.randrange(1,4) # Number of options we want


    user = input('Choose 1 for a Fire Type, 2 for a Water Type, 3 for a Grass Type Pokemon: ') 
    user = int(user) # asking user to choose type

    if user < 1 or user > 3: # Making sure type selection is valid
        print("Thats not a Pokemon type, You've fainted")
    else:
        print("you chose: ", user)
        print("I chose: ", comp)

    #1 Fire Type
    #2 Water Type
    #3 Grass type

    #2 beats 1
    #3 beats 2
    #1 beats 3

    if user== 1:
        if comp == 1:
            print('we tied')
        if comp == 2:
            print ('trainer wins')
        if comp == 3: 
            print ('computer wins')   

    if user== 2:
        if comp == 2:
            print('we tied')
        if comp == 3:
            print ('trainer wins')
        if comp == 1: 
            print ('computer wins')   

    if user== 3:
        if comp == 3:
            print('we tied')
        if comp == 1:
            print ('trainer wins')
        if comp == 2: 
            print ('computer wins')   

    games = games + 1 #adds 1 to game counter

    print('We Played: ', games) #Telling  

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break