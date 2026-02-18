from shop_function import purchasing
from recipe_function import recipeSelect, costSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate               # all the function imports, as well as the customer class, math and random
from difficultySelect import selectDiff
from customerPurchasingEvaluations import customerLoop
from customer_class import Customer
import random as ran
import math as m
import time as t


day = 1 #starting day as 1
difficulty, tax = selectDiff()        #select difficulty; changes starting money + tax amount

inventory = {"money": difficulty, # define starting inventory
             "ice" : 0,
             "lemons" : 0,
             "sugar" : 0,
             "cups": 0}

recipe = {"cost": 0.01, # define base empty recipe
          "ice" : 0,
          "lemons" : 1,
          "sugar" : 0}




while inventory["money"] > 0:       #game loop, each repitition is a day
    print(f"========================================= DAY {day} =========================================")
    displayInv(inventory,0,0,0,0,0,False,0)




    print("========================================= COSTS =========================================")
    prevMoney = inventory["money"]
    inventory = purchasing(inventory)   #daily purchasing
    spent = prevMoney - inventory["money"]




    print("========================================= RECIPE =========================================")
    if day == 1: 
      recipe = recipeSelect()
      recipe = costSelect(recipe)                                                     # recipe changing code
    else:
      while recipeChange != 'n' and recipeChange != 'N' and recipeChange != 'y' and recipeChange != 'Y':
        recipeChange = input('Would you like to edit your recipe? (y/n) ')
      if recipeChange == 'Y' or recipeChange == 'y':
        recipe = recipeSelect()
        recipe = costSelect(recipe)




    cupsMade = maxCupCalculate(recipe,inventory)    # calculate the max amount of cups you can make


    cupsBought = 0                  #customer purchasing loop
    customers = []
    if cupsMade == 0:
      print("You didn't make any cups! You had no customers.")
    for each in range(cupsMade):
      customers.append(Customer)
      purchase, reason = customerLoop(customers[each],recipe)
      if purchase:
        print(f'Customer #{each+1} purchased!')
        cupsBought += 1
        inventory['ice'] -= recipe["ice"]
        inventory['lemons'] -= recipe["lemons"]     
        inventory['sugar'] -= recipe["sugar"]
        inventory["money"] += recipe["cost"]  
        inventory["cups"] -= 1
        displayInv(inventory,0,0,0,0,0,False,0)
      else:
        print(f'Customer #{each+1} did not purchase.')
        print('Reason:',reason)           # return a reason in the function, print it here
        


    profits = recipe["cost"]*cupsBought
    dailyTax = m.floor((tax*(profits/ran.choice([50,30,70,10])))/10) + tax
    inventory["money"] -= dailyTax




    print(f"====================================== DAY {day} RESULTS ======================================")

    displayInv(inventory,recipe,cupsMade,profits,cupsBought,spent,True,dailyTax)                  # daily results

    day += 1

    if inventory["money"] > 0:
      input(f'Pree ENTER to continue to day {day}. ')




else:

  print('You went bankrupt! Goodbye.')            # when you go bankrupt and loop ends, this runs

