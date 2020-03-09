import random, os

clear = lambda: os.system('cls')

state = "bet"
playerSum = 0
houseSum = 0
playerMoney = 1000
card_value = [2,3,4,5,6,7,8,9,10,'J','Q','K','Ace']
hard = False

def GiveCard():
    return random.randint(0,12)

def hit():
    None

while(True): 
    if state == "bet":
        playerCards = []
        houseCards = []
        print("Your account balance is: " + str(playerMoney) + " USD")
        bet = input("How much would you like to place bet: ")

        #Placing bets-------------------------
        try:
            bet = int(bet)

            if playerMoney < bet:
                print("Your desired bet exceed your account balance, please click enter to try again")
            elif bet < 0:
                print("You cannot place bet with negative value, please click enter to try again")
            elif bet == 0:
                print("Your bet needs to be above 0 USD, please click enter to try again")
            else:
                playerMoney -= bet
                state = "firstDeal"
                print("Transaction complete, please click enter to continue")
        except:
            print("You need to input a number, please click enter to try again")

    
    elif state == "firstDeal":
        for i in range(2):
            newPlayerCard = GiveCard()
            newHouseCard  = GiveCard()
            playerCards.append(newPlayerCard)
            houseCards.append(newHouseCard)
        print("Dealer cards are: x and", card_value[houseCards[1]])
        #print("House cards are:",card_value[houseCards[0]], "and", card_value[houseCards[1]])
        print("Your cards are: ", card_value[playerCards[0]], "and", card_value[playerCards[1]])
        #converts the J,Q,K to number 10
        if card_value[playerCards[0]] or card_value[playerCards[1]] or card_value[houseCards[0]] or card_value[houseCards[1]] == 'J' or 'Q' or 'K' or 'Ace':
            card_value[9] = int(10) 
            card_value[10] = int(10)
            card_value[11] = int(10)
    
        #decides if ace will be value of 1 or 11
        if playerSum <= 21:
            card_value[12] = 1
        else:
            card_value[12] = 11
        
        houseSum = card_value[houseCards[0]] + card_value[houseCards[1]]
        playerSum = card_value[playerCards[0]] + card_value[playerCards[1]]

        print()
        print("Your cards =", playerSum)
        #print("Dealar cards =", houseSum)
        print("Dealer cards = x +", card_value[houseCards[1]])
        print()
        #asking if player want to stand or hit
        print("1. Do you want to stand?")
        print("2. Do you want to hit?")
        print("Please input either 1 or 2")
        choice = input()

        if choice == "1":
            state = 'result'
        elif choice == "2":
            state = 'secondDeal'
        else:
            print("You need to input 1 or 2, please click enter to try again")

    elif state == 'result':
        print("Player Sum =", playerSum)
        print("House Sum =", houseSum)

        #checks if you win, if house win and if it is draw
        if(playerSum <= 21 and playerSum > houseSum):
            print("Congratulations, you won!!")
            playerMoney += (bet)*2

            input("Please click enter to continue")
            state = 'bet'
            
        elif playerSum == houseSum:
            print("It is draw")
            playerMoney += bet

            input("Please click enter to continue")
            state = 'bet'
        else:
            print("House wins, better luck next time")

            input("Please click enter to continue")
            state = 'bet'

    elif state == 'secondDeal':
        newPlayerCard = GiveCard()
        playerCards.append(newPlayerCard)
        print("Player cards are: ", card_value[playerCards[0]], "and", card_value[playerCards[1]], "and", card_value[playerCards[2]])
        playerSum = card_value[playerCards[0]] + card_value[playerCards[1]] + card_value[playerCards[2]]
        print("Your cards =", playerSum)
        #print("Dealar cards =", houseSum)
        print("Dealer cards are: x and", card_value[houseCards[1]])

        print("1. Please input 1 to continue")
        choice = input()

        if choice == "1":
            state = 'result'
            
    input()
    clear()
    