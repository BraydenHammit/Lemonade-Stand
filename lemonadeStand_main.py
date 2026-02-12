from shop_function import purchasing
from recipe_function import recipeSelect, costSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate               # all the function imports and math + random
from difficultySelect import selectDiff
from customerPurchasingEvaluations import customerLoop
import random as ran
import math as m

day = 1
difficulty = selectDiff()

inventory = {"money": difficulty, # definines the inventory for later use in the total over arching code
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

    displayInv(inventory,0,0,0,0,0,False)

    print('==========================================================================================')

    prevMoney = inventory["money"]

    inventory = purchasing(inventory)   #daily purchasing

    spent = prevMoney - inventory["money"]
    
    recipe = recipeSelect()
    
    recipe = costSelect(recipe)

    cupsMade = maxCupCalculate(recipe,inventory)

    cupsBought = 0                  #UNFINISHED customer purchasing code
    customers = []
    for each in range(m.floor(cupsMade)):
      
      cupsBought += 1

    inventory['ice'] -= recipe["ice"]*cupsBought
    inventory['lemons'] -= recipe["lemons"]*cupsBought
    inventory['sugar'] -= recipe["sugar"]*cupsBought

    profits = recipe["cost"]*cupsBought   
    inventory["money"] += profits

    print("==========================================================================================")

    displayInv(inventory,recipe,cupsMade,profits,cupsBought,spent,True)

    day += 1