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
    
    recipe = {"ice" : int(input('How much ice would you like to use per cup?')),
          "lemons" : int(input('How many lemons would you like to use per cup?')),
          "sugar" : int(input('How much sugar would you like to use per cup?'))}

    cupsBought = ran.randint(0,30)   #replace when we get customer code
    
    inventory['ice'] -= recipe["ice"]*cupsBought
    inventory['lemons'] -= recipe["lemons"]*cupsBought
    inventory['sugar'] -= recipe["sugar"]*cupsBought

    recipe = recipeSelect(recipe)
    
    recipe = costSelect(recipe)

    cupsMade = maxCupCalculate(recipe,inventory)

    profits = recipe["cost"]*cupsMade   #replace when we get customer code
    recipe["cost"] += profits

    displayInv(inventory,recipe,cupsMade, profits)