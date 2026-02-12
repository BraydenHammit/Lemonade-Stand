def recipeSelect():
    recipe = {"ice" : -1,
          "lemons" : -1,
          "sugar" : -1}

    lemons = 0
    while lemons <= 0 or lemons >= 4:
        try:
            lemons = int(input("How many lemons do you want to use per cup? (Between 1 and 3) "))
        except:
            print('Invalid amount!')
            lemons = 0
    recipe["lemons"] = lemons

    ice = -1
    while ice <= -1 or ice >= 4:
        try:
            ice = int(input("How much ice do you want to use per cup? (Between 0 and 3) "))
        except:
            print('Invalid amount!')
            ice = -1
    recipe["ice"] = ice

    sugar = -1
    while sugar <= -1 or sugar >= 4:
        try:
            sugar = int(input("How much sugar do you want to use per cup? (Between 0 and 3) "))
        except:
            print('Invalid amount!')
            sugar = -1
    recipe["sugar"] = sugar

    return recipe

def costSelect(recipe):
    cost = 0
    while cost <= 0 or cost >= 2.51:
        try:
            cost = float(input("How much do you want each cup of lemonade to cost? (Can't be larger than 2.5) "))
        except:
            print('Invalid cost!')
            cost = 0
    recipe["cost"] = cost
    return recipe