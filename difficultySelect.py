def selectDiff():
    print('==========================================================================================')

    difficulty = int(input('Please choose a difficulty:\nEasy - 1\nMedium - 2\nHard - 3\n'))
    
    while difficulty <= 0 or difficulty > 3:
        try:
            difficulty = int(input('Please choose a difficulty: '))
        except ValueError:
            print('Invalid answer!')

    if difficulty == 1:
        difficulty = 300
    elif difficulty == 2:
        difficulty = 175
    else:
        difficulty = 50

    return difficulty