import random 


space = ["Go","Mediterranean Avenue","Community Chest","Baltic Avenue","Income Tax","Reading Railroad","Oriental Avenue","Chance",
                "Vermont Avenue","Connecticut Avenue","Jail / Just Visiting","St. Charles Place","Electric Company","States Avenue","Virginia Avenue",
                "Pennsylvania Railroad","St. James Place","Community Chest","Tennessee Avenue","New York Avenue","Free Parking","Kentucky Avenue",
                "Chance","Indiana Avenue","Illinois Avenue","B. & O. Railroad","Atlantic Avenue","Ventnor Avenue","Water Works","Marvin Gardens",
                "Go To Jail","Pacific Avenue","North Carolina Avenue","Community Chest","Pennsylvania Avenue","Short Line","Chance","Park Place",
                "Luxury Tax","Boardwalk"]

def startGame(locations):
    index = 0
    spaceLength = len(space)
    twelveTracker = 0
            
    while True:
        dice1 = random.randrange (1, 7)
        dice2 = random.randrange(1,7)
              
        sum = dice1 + dice2
    
        print("Dice: " + str(dice1) + " "  + " Dice: "+ str(dice2) )
        if (sum == 12): 
            twelveTracker = twelveTracker + 1
            if (twelveTracker == 3):
                print("You go to Jail Now!. Game Over")
                break
            
        index += sum
        if (index < spaceLength-1):
            print("You landed on " + space[index]+". Keep going!")
            
        elif (index == spaceLength-1):
            print("Landed on " +  space[index] + ". Win!!!!")
            break
        else:
            index = index - spaceLength
            print("Passing the circle. " +  "Currently landed on " +  space[index])
    
startGame(space)
