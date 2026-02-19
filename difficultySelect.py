def selectDiff():
    print("======================================= DIFFICULTY =======================================")

    try:
        difficulty = int(input('Please choose a difficulty:\nEffortless - 0\nEasy - 1\nNormal - 2\nHard - 3\nImpossible - 4\nRemorseless - 5\n'))
    except ValueError:
            print('Invalid answer!')
    
    
    while difficulty <= 0 or difficulty > 4:
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
    if difficulty == 1:
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
    else:
        difficulty = 3
        tax = 25

    return difficulty, tax