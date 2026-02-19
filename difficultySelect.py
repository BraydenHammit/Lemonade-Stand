def selectDiff():
    print("======================================= DIFFICULTY =======================================")
    print('Difficulties:\nEffortless - 0\nEasy - 1\nNormal - 2\nHard - 3\nImpossible - 4\nRemorseless - 5')
    
    difficulty = 648503.965
    
    while difficulty < 0 or difficulty > 5:
        if difficulty != 648503.965:
            print('Invalid number!')
        try:
            difficulty = int(input('Please choose a difficulty: '))
        except ValueError:
            print('Invalid answer!')
            difficulty = 648503.965 #set to this so it doesn't also print invalid number (which should only print if its a number below 0 or above 5)


    if difficulty == 0:         #set difficulty to starting money, return that to set the starting inventory
        difficulty = 7500
        tax = 0.5
    elif difficulty == 1:
        difficulty = 300
        tax = 2
    elif difficulty == 2:
        difficulty = 175
        tax = 3.5
    elif difficulty == 3:
        difficulty = 50
        tax = 5
    elif difficulty == 4:
        difficulty = 15
        tax = 6.5
    elif difficulty == 5:
        difficulty = 3
        tax = 7.5

    return difficulty, tax