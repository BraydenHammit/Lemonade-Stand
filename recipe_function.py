def recipeSelect():
    recipe = {"ice" : -1,
          "lemons" : -1,
          "sugar" : -1}

    lemons = 0
    while lemons <= 0 or lemons >= 4:
        if lemons != -1.4:
            print('Invalid amount!')
        try:
            lemons = int(input("How many lemons do you want to use per cup? (Between 1 and 3) "))
        except:
            print('Invalid amount!')
            lemons = -1.4
    recipe["lemons"] = lemons

    ice = -1
    while ice <= -1 or ice >= 4:
        if ice != -1.4:
            print('Invalid amount!')
        try:
            ice = int(input("How much ice do you want to use per cup? (Between 0 and 3) "))
        except:
            print('Invalid amount!')
            ice = -1.4
    recipe["ice"] = ice

    sugar = -1
    while sugar <= -1 or sugar >= 4:
        if sugar != -1.4:
            print('Invalid amount!')
        try:
            sugar = int(input("How much sugar do you want to use per cup? (Between 0 and 3) "))
        except:
            print('Invalid amount!')
            sugar = -1.4
    recipe["sugar"] = sugar

    return recipe

def costSelect(recipe):
    cost = 0
    while cost <= 0 or cost >= 2.51:
        if cost != 3546:
            print('Invalid amount!')
        try:
            cost = float(input("How much do you want each cup of lemonade to cost? (Between 0.01 and 2.50) "))
        except:
            print('Invalid cost!')
            cost = 3546
    recipe["cost"] = cost
    return recipe