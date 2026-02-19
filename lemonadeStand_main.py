from shop_function import purchasing
from recipe_function import recipeSelect
from inventoryDisplay import displayInv
from maxCups import maxCupCalculate               # all the function imports, as well as the customer class, math and random
from difficultySelect import selectDiff
from customerPurchasingEvaluations import customerLoop
from achievements.diplomas import diplomaY, diplomaM
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
      recipeChange = 'n/a'
      while recipeChange != 'n' and recipeChange != 'N' and recipeChange != 'y' and recipeChange != 'Y':
        recipeChange = input('Would you like to edit your recipe? (y/n) ')
        if recipeChange != 'n' and recipeChange != 'N' and recipeChange != 'y' and recipeChange != 'Y':
          print('Invalid answer!')
      if recipeChange == 'Y' or recipeChange == 'y':
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

      t.sleep(0.1)
        


    profits = recipe["cost"]*cupsBought
    print("========================================== TAXES ==========================================")
    evade = 'n/a'
    dailyTax = m.floor((tax*(profits/ran.choice([50,30,70,10])))/10) + tax        #tax calculation
    while evade != 'n' and evade != 'N' and evade != 'y' and evade != 'Y':
      evade = input(f'Would you like to attempt to evade your taxes of {dailyTax}? (y/n) ')
      if evade != 'n' and evade != 'N' and evade != 'y' and evade != 'Y':           #tax evasion decision code
        print('Invalid answer!')
    if evade == 'Y' or evade == 'y':
      if ran.randint(1,3) == 3:       # 33% chance to succeed in evading
        print('You...succeeded. ')
        t.sleep(3)
        print("Don't do it again.")
        t.sleep(3)
        dailyTax = 0
      else:
        death = 'tax evasion'
        break     #break and print death screen
    else:
      inventory["money"] -= dailyTax          #apply tax if not evaded




    print(f"====================================== DAY {day} RESULTS ======================================")

    displayInv(inventory,recipe,cupsMade,profits,cupsBought,spent,True,dailyTax)                  # daily results

    if day == 30:   # 1 month achievement tkinter image
      diplomaM()
    if day == 365:    # 1 year achievement tkinter image
      diplomaY()

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
    

print("========================================== DEATH ==========================================")

# when you die and the loop ends, one of these runs:
if death == 'bankrupt':
  print('You ran out of money, and had to close your lemonade stand.\nLike I said, you went bankrupt. Goodbye!')            
elif death == 'permit':
  print('Your permit ran out, and your earnings were confiscated!\nYou went bankrupt. Goodbye!')
elif death == 'forfeit':
  print('You forfeit your lemonade stand and donated all profits to charity.\nIt was a kind move, but it left you broke; you went bankrupt. Goodbye!')
elif death == 'tax evasion':
  print("You tried. You failed. Tax evasion isn't the answer. The IRS confiscated your earnings.\nYou went bankrupt. Goodbye...criminal.")


print("===========================================================================================")
