def selectDiff():
    print('==========================================================================================')

    try:
        difficulty = int(input('Please choose a difficulty:\nEasy - 1\nMedium - 2\nHard - 3\n'))
    except ValueError:
            print('Invalid answer!')
    
    
    while difficulty <= 0 or difficulty > 3:
        if difficulty != 6485:
            print('Invalid number!')
        try:
            difficulty = int(input('Please choose a difficulty: '))
        except ValueError:
            print('Invalid answer!')
            difficulty = 6485

    if difficulty == 1:
        difficulty = 300
    elif difficulty == 2:
        difficulty = 175
    else:
        difficulty = 50

    return difficulty