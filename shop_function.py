def purchasing(inventory):
    purchaseType = 'n/a'

    print('Ice - 0.75\nLemons - 1.00\nSugar - 0.50\nCups - 0.25')

    while purchaseType != 'done':
        print("========================================== SHOP ==========================================")

        purchaseType = input('What would you like to buy? Ice, lemons, sugar, or cups? (i/l/s/c/done) ')

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
            if inventory["money"] - .75*purchaseAmount > 0:
                inventory["money"] -= .75*purchaseAmount
                inventory["ice"] += purchaseAmount
            else:
                print('Too expensive!')

        elif purchaseType == 'l':
            if inventory["money"] - 1*purchaseAmount > 0:
                inventory["money"] -= 1*purchaseAmount
                inventory["lemons"] += purchaseAmount
            else:
                print('Too expensive!')

        elif purchaseType == 's':
            if inventory["money"] - .5*purchaseAmount > 0:
                inventory["money"] -= .5*purchaseAmount
                inventory["sugar"] += purchaseAmount
            else:
                print('Too expensive!')

        elif purchaseType == 'c':
            if inventory["money"] - .25*purchaseAmount > 0:
                inventory["money"] -= .25*purchaseAmount
                inventory["cups"] += purchaseAmount
            else:
                print('Too expensive!')
        
        elif not valid:
            print('Invalid item!')
        
        print(f'Money: {inventory["money"]} \nLemons: {inventory["lemons"]} \nIce: {inventory["ice"]} \nSugar: {inventory["sugar"]} \nCups: {inventory["cups"]}')
    
    return inventory
