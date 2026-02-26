def recipeSelect():
    recipe = {"ice" : -1.4,
          "lemons" : -1.4,
          "sugar" : -1.4}

    recipe["lemons"] = ingredient(1,3,'lemons')
    recipe["ice"] = ingredient(0,3,'ice')
    recipe["sugar"] = ingredient(0,3,'sugar')
    recipe["water"] = ingredient(25,1000,'water')
    recipe["cost"] = ingredient(0.01,3.5,'cost')

    return recipe


def ingredient(min,max,type):
    if type == 'cost':
        ingred = 3456
    else:
        ingred = -1.4
    while ingred < min or ingred > max:
        if (ingred != -1.4 and type != 'cost') or (ingred != 3456 and type == 'cost'):
            print('Invalid amount!')
        try:
            if type == 'water':
                ingred = int(input("How much water do you want to use per cup? (Between 25 and 1000 milliliters.) "))
            elif type == 'lemons':
                ingred  = int(input("How many lemons do you want to use per cup? (Between 1 and 3 lemons.) "))
            elif type == 'sugar':
                ingred = int(input("How much sugar do you want to use per cup? (Between 0 and 3 grams.) "))
            elif type == 'ice':
                ingred = int(input("How much ice do you want to use per cup? (Between 0 and 3 cubes.) "))
            elif type == 'cost':
                ingred = float(input("How much do you want each cup of lemonade to cost? (Between 0.01 and 3.50) "))
        except ValueError:
            print('Invalid amount!')
            if type == 'cost':
                ingred = 3456
            else:
                ingred = -1.4
    
    return ingred