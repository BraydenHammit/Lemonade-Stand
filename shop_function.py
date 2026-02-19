def purchasing(inventory):
    purchaseType = 'n/a'

    print('Lemons - 1.00\nIce - 0.75\nSugar - 0.50\nCups - 0.25\nPermit Renweal - 5.00')
    if inventory["permit"] == 0:
        print('Note: Your permit is about to expire! You have to renew it today!')
    else:
        print(f'Note: You have {inventory["permit"]} days left until your permit runs out.')

    while purchaseType != 'done':
        print("========================================== SHOP ==========================================")




        purchaseType = input('What would you like to buy? Ice, lemons, sugar, cups, or renew your permit? (i/l/s/c/p/done) ') #add a permit that is required and you must renew every 7 days (for like 5 bucks)

        if (purchaseType != 'done') and (purchaseType != 'i') and (purchaseType != 'l') and (purchaseType != 's') and (purchaseType != 'c') and (purchaseType != 'p'):
            valid = False
        else:
            valid = True



        if (purchaseType != 'done') and (purchaseType != 'p') and valid:
            try:
                purchaseAmount = int(input('How many would you like to buy? '))
                    
            except ValueError:    
                print("Invalid answer!")




        if purchaseType == 'i':
            purchase("ice", purchaseAmount, inventory, 0.75)

        elif purchaseType == 'l':
            purchase("lemons", purchaseAmount, inventory, 1)

        elif purchaseType == 's':
            purchase("sugar", purchaseAmount, inventory, 0.5)

        elif purchaseType == 'c':
            purchase("cups", purchaseAmount, inventory, 0.25)
        
        elif purchaseType == 'p':
            purchase("permit", 1, inventory, 0.5)
        



        elif not valid:
            print('Invalid item!')
        
        print(f'Money: {inventory["money"]} \nLemons: {inventory["lemons"]} \nIce: {inventory["ice"]} \nSugar: {inventory["sugar"]} \nCups: {inventory["cups"]}')
    
    return inventory



def purchase(type, amount, inventory, cost):
    if inventory["money"] - cost*amount > 0:
        inventory["money"] -= cost*amount
        if type == 'permit':
            inventory[type] = 7
        else:
            inventory[type] += amount
    else:
        print('Too expensive! Try again.')