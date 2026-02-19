def recipeSelect():
    recipe = {"ice" : -1.4,
          "lemons" : -1.4,
          "sugar" : -1.4}

    recipe["lemons"] = ingredient(1,3,'lemons')
    recipe["ice"] = ingredient(0,3,'ice')
    recipe["sugar"] = ingredient(0,3,'sugar')
    recipe["water"] = ingredient(25,500,'water')

    return recipe


def ingredient(min,max,type):
    ingred = -1.4
    while ingred < min or ingred > max:
        if ingred != -1.4:
            print('Invalid amount!')
        try:
            if type == 'water':
                ingred = int(input("How much water do you want to use per cup? (Between 25 and 500 milliliters.) "))
            elif type == 'lemons':
                ingred  = int(input("How many lemons do you want to use per cup? (Between 1 and 3 lemons.) "))
            elif type == 'sugar':
                ingred = int(input("How much sugar do you want to use per cup? (Between 0 and 3 grams.) "))
            elif type == 'ice':
                ingred = int(input("How much ice do you want to use per cup? (Between 0 and 3 cubes.) "))
        except ValueError:
            print('Invalid amount!')
            ingred = -1.4
    
    return ingred





def costSelect(recipe):
    cost = 3546
    while cost <= 0 or cost >= 3.01:
        if cost != 3546:
            print('Invalid amount!')
        try:
            cost = float(input("How much do you want each cup of lemonade to cost? (Between 0.01 and 3.00) "))
        except ValueError:
            print('Invalid cost!')
            cost = 3546
    recipe["cost"] = cost
    return recipe