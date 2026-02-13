def selectDiff():
    print("======================================= DIFFICULTY =======================================")

    try:
        difficulty = int(input('Please choose a difficulty:\nEasy - 1\nMedium - 2\nHard - 3\n'))
    except ValueError:
            print('Invalid answer!')
    
    
    while difficulty <= 0 or difficulty > 3:
        if difficulty != 648503.965:
            print('Invalid number!')
        try:
            difficulty = int(input('Please choose a difficulty: '))
        except ValueError:
            print('Invalid answer!')
            difficulty = 648503.965

    if difficulty == 1:
        difficulty = 300
        tax = 53.5
    elif difficulty == 2:
        difficulty = 175
        tax = 5
    else:
        difficulty = 50
        tax = 7

    return difficulty, tax