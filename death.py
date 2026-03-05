def died(death):
    print("=========================================== END ===========================================")

    # when you die and the loop ends, one of these runs:
    if death == 'bankrupt':
        print('You ran out of money, and had to close your lemonade stand.\nLike I said, you went bankrupt. Goodbye!')            
    elif death == 'permit':
        print('Your permit ran out, and your earnings were confiscated!\nYou went bankrupt. Goodbye!')
    elif death == 'forfeit':
        print('You forfeit your lemonade stand and donated all profits to charity.\nIt was a kind move, but it left you broke; you went bankrupt. Goodbye!')
    elif death == 'tax evasion':
        print("You tried. You failed. Tax evasion isn't the answer. The IRS confiscated \nall of your earnings. You went bankrupt. Goodbye...criminal.")
    elif death == '50k quit':
        print("You won! It was an honor being your narrator. Thank you.\nThough I hate to see you go, your journey has come to an end.\nYou survived. You didn't go bankrupt. Goodbye...")
    elif death == 'week quit':
        print("You survived a week, then quit. Maybe you found another job.\nMaybe you didn't. Though, you didn't go bankrupt. Goodbye!")


    print("===========================================================================================")