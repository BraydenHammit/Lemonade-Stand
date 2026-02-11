from shop_function import purchasing
from recipe_function import recipeSelect, costSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate
import random as ran

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
    inventory = purchasing(inventory)   #daily purchasing
    
    recipe = {"ice" : -1,
          "lemons" : -1,
          "sugar" : -1}

    recipe = recipeSelect(recipe)
    
    recipe = costSelect(recipe)

    cupsMade = maxCupCalculate(recipe,inventory)

    cupsBought = 0                  #UNFINISHED customer purchasing code
    for each in range(cupsMade):
      cupsBought+=1

    inventory['ice'] -= recipe["ice"]*cupsBought
    inventory['lemons'] -= recipe["lemons"]*cupsBought
    inventory['sugar'] -= recipe["sugar"]*cupsBought

    profits = recipe["cost"]*cupsBought   
    recipe["cost"] += profits

    displayInv(inventory,recipe,cupsMade,profits,cupsBought)