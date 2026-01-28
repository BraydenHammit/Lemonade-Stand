import shop_function as shopF
import random as ran

inventory = {"money": 100,
             "ice" : 0,
             "lemons" : 0,
             "sugar" : 0}

while inventory["money"] > 0:       #game loop, each repitition is a day
    list = shopF.purchasing(inventory["money"],[inventory["ice"],inventory["lemons"],inventory["sugar"]])   #daily purchasing

    inventory["money"] = list[0]
    inventory["ice"] = list[1][0]
    inventory["lemons"] = list[1][1]
    inventory["sugar"] = list[1][2]

    inventory["money"] += ran.randint(0,5)   #replace when we get customer code

    print('Money:',inventory["money"])
    print('Ice:',inventory["ice"])
    print('Lemons:',inventory["lemons"])         #print inventory
    print('Sugar:',inventory["sugar"])