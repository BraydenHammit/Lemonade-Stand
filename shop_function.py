def purchasing(inventory):
    purchaseType = 'n/a'

    while purchaseType != 'done':
        print('=============================')


        valid = False
        while not valid:
            purchaseType = input('What would you like to buy? Ice, lemons, sugar, water, cups, or a permit renewal? (i/l/s/w/c/p/done) ') #add a permit that is required and you must renew every 7 days (for like 5 bucks)

            if (purchaseType != 'done') and (purchaseType != 'i') and (purchaseType != 'l') and (purchaseType != 's') and (purchaseType != 'c') and (purchaseType != 'p') and (purchaseType != 'w'):
                valid = False
                print('Invalid item!')
            else:
                valid = True            #check if the answer was one of the allowed answers (i/l/s/w/c/p/done)



        if (purchaseType != 'done') and (purchaseType != 'p') and valid:
            valid = False
            while not valid:
                try:
                    purchaseAmount = int(input('How many/much would you like to buy? '))
                    valid = True
                        
                except ValueError:    
                    print("Invalid answer!")
                    valid = False





        if purchaseType == 'i':
            purchase("ice", purchaseAmount, inventory, 0.5)

        elif purchaseType == 'l':
            purchase("lemons", purchaseAmount, inventory, 0.75)

        elif purchaseType == 's':
            purchase("sugar", purchaseAmount, inventory, 0.25)

        elif purchaseType == 'c':
            purchase("cups", purchaseAmount, inventory, 0.1)
            
        elif purchaseType == 'p':
            purchase("permit", 1, inventory, 5)

        elif purchaseType == 'w':
            purchase("water", purchaseAmount, inventory, 0.01)



        
        print(f'Money: {inventory["money"]} \nLemons: {inventory["lemons"]} \nIce: {inventory["ice"]} \nSugar: {inventory["sugar"]} \nWater: {inventory["water"]} \nCups: {inventory["cups"]}')               #print inventory between purchases
    
    return inventory



def purchase(type, amount, inventory, cost):            #purchasing function, used above ^
    if inventory["money"] - cost*amount > 0:
        inventory["money"] -= cost*amount
        inventory["money"] = round(inventory["money"],2)
        if type == 'permit':
            inventory[type] = 7             #only if renewing permit, do this
            print('Your permit has been renewed! Make sure to renew it again within 7 days.')
        elif type == 'water':
            inventory[type] += amount*100
        else:
            inventory[type] += amount
    else:
        print('Too expensive! Try again.')