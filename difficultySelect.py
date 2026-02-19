def selectDiff():
    print("======================================= DIFFICULTY =======================================")
    print('Difficulties:\nEffortless - 0\nEasy - 1\nNormal - 2\nHard - 3\nImpossible - 4\nRemorseless - 5')
    
    difficulty = 648503.965
    
    while difficulty <= -1 or difficulty > 5:
        if difficulty != 648503.965:
            print('Invalid number!')
        try:
            difficulty = int(input('Please choose a difficulty: '))
        except ValueError:
            print('Invalid answer!')
            difficulty = 648503.965


    if difficulty == 0:
        difficulty = 7500
        tax = 0.5
    elif difficulty == 1:
        difficulty = 300
        tax = 3.5
    elif difficulty == 2:
        difficulty = 175
        tax = 5
    elif difficulty == 3:
        difficulty = 50
        tax = 7
    elif difficulty == 4:
        difficulty = 15
        tax = 10
    elif difficulty == 5:
        difficulty = 3
        tax = 25

    return difficulty, tax