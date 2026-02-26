from shop_function import purchasing
from recipe_function import recipeSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate               # all the function imports, as well as the customer class, math and random
from difficultySelect import selectDiff
from customerPurchasingEvaluations import customerLoop
from achievements.achievements import achievementY, achievementM
from death import died
from yesNoLoop import taxes, changeR
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
             "cups": 0,
             "water": 0,
             "permit": 7}

recipe = {"cost": 0.01, # define base empty recipe
          "ice" : 0,
          "lemons" : 1,
          "sugar" : 0,
          "water": 25}




while inventory["money"] > 0:       #game loop, each repitition is a day
    print(f"========================================= DAY {day} =========================================")
    displayInv(inventory,0,0,0,0,0,False,0)         #show inventory at start of day



    prevMoney = inventory["money"]
    inventory = purchasing(inventory)   #daily purchasing
    spent = prevMoney - inventory["money"]




    print("========================================= RECIPE =========================================")
    if day == 1: 
      recipe = recipeSelect()                                                  # recipe/cost changing code
    else:
      recipeChange = changeR()
      if recipeChange:
        recipe = recipeSelect()




    cupsMade = maxCupCalculate(recipe,inventory)    # calculate the max amount of cups you can make

    cupsBought = 0                  #customer purchasing loop
    customers = []
    print("======================================== CUSTOMERS =======================================")

    if cupsMade == 0:
      print("You didn't make any cups! You had no customers.")

    for each in range(cupsMade):
      customers.append(Customer())
      purchase, reason = customerLoop(customers[each],recipe)
      
      if purchase:
        print(f'Customer #{each+1} purchased!')
        cupsBought += 1
        inventory['ice'] -= recipe["ice"]
        inventory['lemons'] -= recipe["lemons"]     #print new info if they purchase
        inventory['sugar'] -= recipe["sugar"]
        inventory['water'] -= recipe["water"]
        inventory["money"] += recipe["cost"]  
        inventory["cups"] -= 1
        displayInv(inventory,0,0,0,0,0,False,0)

      else:
        print(f'Customer #{each+1} did not purchase.')
        print('Reason(s):')             #print reasons of why they didn't purchase if they didn't
        for rsn in reason:
          print(' ',rsn)

      if each != cupsMade-1:
        print('=============================')

      if cupsMade <= 500:
        t.sleep(0.1)
      elif cupsMade <= 2500:
        t.sleep(0.025)
      else:
        t.sleep(0.001)
        


    profits = recipe["cost"]*cupsBought
    dailyTax = m.floor(tax*(profits/ran.randint(10,20))) + tax          #tax calculation
    inventory, dailyTax = taxes(inventory, dailyTax)
    if inventory == 'death':
      death = 'tax evasion'
      break




    print(f"====================================== DAY {day} RESULTS ======================================")

    displayInv(inventory,recipe,cupsMade,profits,cupsBought,spent,True,dailyTax)                  # daily results

    if day == 30:   # 1 month achievement tkinter image
      achievementM()
    if day == 365:    # 1 year achievement tkinter image
      achievementY()

    day += 1         #add a day to count at end of each day
    inventory["permit"] -= 1.  #permit countdown, -1 each day
    
    if inventory["permit"] < 0:
      death = 'permit'
      break       # death screen if you forget to renew your permit

    if inventory["money"] > 0:
      quit = input(f'Press ENTER to continue to day {day}, or type QUIT to quit. ')       #pause in between days, give option to quit
    else:
      death = 'bankrupt'
      break     #death screen if bankrupt

    if quit == 'QUIT':
      death = 'forfeit'
      break     #death screen if you quit
    


died(death)