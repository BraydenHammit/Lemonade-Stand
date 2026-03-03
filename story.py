import time as t
from yesNoLoop import loopYN

def story(story,ext,name):
    print("========================================= STORY ==========================================")
    if story == 1:
        print(f"On a trip to Vegas, you and your friend {name} made a million dollars each. \nYou then took a risky gamble. You bet it all on black 32.")
        t.sleep(5.64)
        print("You won. It doubled. You bet it again. It doubled. You bet it again...")
        t.sleep(3.5)
        print("You lost it all. You left with a total of fifty thousand dollars in debt. \nIn attempt to pay off your debt, you set up a lemonade stand. Don't go bankrupt.")
    elif story == 2:
        print(f"Your friend {name} made a bet that you couldn't make fifty thousand dollars. \nHe said you should open a lemonade stand, and make fifty thousand.")
        loopYN('b')
        if ext == 1:
            print("You accept the bet. From there begins probably the most legendary... \nWait, that's the wrong script. What I meant was:")
            t.sleep(2.35)
        print("You accept the bet. From there begins your lemonade stand. Don't go bankrupt.")

    t.sleep(3)