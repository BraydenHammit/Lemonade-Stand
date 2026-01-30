from shop_function import purchasing
from recipe_function import recipeSelect, costSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate

inventory = {"money": 100,
             "ice" : 0,
             "lemons" : 0,
             "sugar" : 0,
             "cups": 0}

recipe = {"cost": 1,
          "ice" : 0,
          "lemons" : 1,
          "sugar" : 0}

while inventory["money"] > 0:       #game loop, each repitition is a day

    inventory = purchasing(inventory)   #daily purchasing

    recipe = recipeSelect(recipe)
    
    recipe = costSelect(recipe)

    cupsMade = maxCupCalculate(recipe,inventory)

    profits = recipe["cost"]*cupsMade   #replace when we get customer code
    recipe["cost"] += profits

    displayInv(inventory,recipe,cupsMade, profits)