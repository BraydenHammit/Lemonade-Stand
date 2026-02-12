from shop_function import purchasing
from recipe_function import recipeSelect, costSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate
import random as ran

day = 1
import math as m

inventory = {"money": 100, # definines the inventory for later use in the total over arching code
             "ice" : 0,
             "lemons" : 0,
             "sugar" : 0,
             "cups": 0}

recipe = {"cost": 1, # definines the recipe for use in the branching code
          "ice" : 0,
          "lemons" : 1,
          "sugar" : 0}

while inventory["money"] > 0:       #game loop, each repitition is a day
    print(f"========================================= DAY {day} =========================================")

    displayInv(inventory,0,0,0,0,False)

    print('==========================================================================================')

    inventory = purchasing(inventory)   #daily purchasing
    
    recipe = {"ice" : -1,
          "lemons" : -1,
          "sugar" : -1}

    recipe = recipeSelect(recipe)
    
    recipe = costSelect(recipe)

    cupsMade = maxCupCalculate(recipe,inventory)

    cupsBought = 0                  #UNFINISHED customer purchasing code
    for each in range(m.floor(cupsMade)):
      cupsBought+=1

    inventory['ice'] -= recipe["ice"]*cupsBought
    inventory['lemons'] -= recipe["lemons"]*cupsBought
    inventory['sugar'] -= recipe["sugar"]*cupsBought

    profits = recipe["cost"]*cupsBought   
    recipe["cost"] += profits

    print("==========================================================================================")

    displayInv(inventory,recipe,cupsMade,profits,cupsBought,True)

    day += 1