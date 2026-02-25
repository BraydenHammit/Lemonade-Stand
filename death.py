def died(death):
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