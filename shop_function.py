def purchasing(inventory):
    purchaseType = 'n/a'

    print('Ice - 0.75\nLemons - 1.00\nSugar - 0.50\nCups - 0.25')

    while purchaseType != 'done':
        print("========================================== SHOP ==========================================")




        purchaseType = input('What would you like to buy? Ice, lemons, sugar, or cups? (i/l/s/c/done) ') #add a permit that is required and you must renew every 7 days (for like 5 bucks)

        if (purchaseType != 'done') and (purchaseType != 'i') and (purchaseType != 'l') and (purchaseType != 's') and (purchaseType != 'c'):
            valid = False
        else:
            valid = True



        if (purchaseType != 'done') and (valid):
            try:
                purchaseAmount = int(input('How many would you like to buy? '))
                    
            except ValueError:    
                print("Invalid amount!")




        if purchaseType == 'i':
            purchase("ice", purchaseAmount, inventory, 0.75)

        elif purchaseType == 'l':
            purchase("lemons", purchaseAmount, inventory, 1)

        elif purchaseType == 's':
            purchase("sugar", purchaseAmount, inventory, 0.5)

        elif purchaseType == 'c':
            purchase("cups", purchaseAmount, inventory, 0.25)
        



        elif not valid:
            print('Invalid item!')
        
        print(f'Money: {inventory["money"]} \nLemons: {inventory["lemons"]} \nIce: {inventory["ice"]} \nSugar: {inventory["sugar"]} \nCups: {inventory["cups"]}')
    
    return inventory

def purchase(type, amount, inventory, cost):
    if inventory["money"] - cost*amount > 0:
        inventory["money"] -= cost*amount
        inventory[type] += amount
    else:
        print('Too expensive! Try again.')