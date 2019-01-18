def makeHouse(fname):
    print(fname)
    fileRoom = open(fname)
      
    topFloor = str(fileRoom.readline())
    mainFloor = str(fileRoom.readline())
    basement = str(fileRoom.readline())

    topFloor = topFloor.strip().split(',')
    mainFloor = mainFloor.strip().split(',')
    basement = basement.strip().split(',')

    print("Top Floor :  ", topFloor)
    print("Main :  " , mainFloor)
    print("Basement:  " , basement)
    
    fileRoom.close()
    
    return topFloor, mainFloor, basement

def keyLocation(top, main, basement):

    import random

    topFloor = top[random.randint(2 , len(top) - 1)]

    mainFloor = main[random.randint(3 , len(main) - 1)]

    basementFloor = basement[random.randint(2 , len(basement) - 1)]

    return topFloor, mainFloor, basementFloor
  

def introduction():
   
    print("You have awoken in a mysterious house.")
    print("You check the front door and find out it is locked.")
    print("The door needs 3 keys to open.")
    print("You will need to search the house for 3 keys in order to free yourself from the house.")
    print("The house has two floors and a basement.\n")

    print("Type Exit at any time to exit the game.\n")

    return

def floor(roomList , key , keyFound):

    roomsSearched = 0

    floor = roomList[0]
    
    rooms = roomList
    
    cheat = False
    
    floor = floor.strip()
    floor = floor.title()
    foundKey = keyFound
    # keyLocation = key
    plusKey = 0

    validInput = False
        
    print("Choose a location to search. Current Location - " , floor)
    
    print("[", end=" ")
    for i in range(len(rooms) -1):
        if i == (len(rooms) - 2):
            print(rooms[i+1], end="")
        else:
            print(rooms[i+1], end=" , ")
            
    print(" ]\n")
        

    userInput = input()
    
    userInput = userInput.strip()
    userInput = userInput.title()

    print("\n")

    

    if userInput == key:
        if keyFound == False:
            foundKey = True
            plusKey = 1

            roomsSearched = roomsSearched + 1
            
        else:
            print("\nKey already found a key in this room. Search another room in the house\n")

            roomsSearched = roomsSearched + 1

    elif userInput == 'Upstairs':

        print("You go up the stairs.\n")

        if floor == 'Main Floor':
            floor = 'Upstairs'
        elif floor == 'Basement':
            floor = 'Main Floor'
            

    elif userInput == 'Downstairs':

        print("You go down the stairs.\n")

        if floor == 'Main Floor':

            floor = 'Basement'

        elif floor == 'Upstairs':

            floor = 'Main Floor'


    elif userInput == "Exit":
        floor = "Exit"

    elif userInput == "Cheater":
        
        cheat = True
        
    else:

        for i in range(len(rooms)):
            if rooms[i] == userInput:
                validInput = True

        if validInput == True:
            roomsSearched = roomsSearched + 1
            print("\nNo Key Found\n")

        else:
            print("\nInvalid Room Entered, please type in a correct room\n")


    floor = floor.strip()
    floor = floor.title()


    return foundKey , floor, plusKey, roomsSearched, cheat


    
def main():

    programRun = True

    topFloor, mainFloor, basementFloor = makeHouse("D:/projects/ela/Tutorials/python/Game_Rooms.txt")
    
    topLocation , mainLocation, basementLocation = keyLocation(topFloor, mainFloor, basementFloor)

    keyTop = False
    keyMain = False
    keyBasement = False

    addKey = int()

    totalKeys = 0

    keysLeft = 3

    currentFloor = "Main Floor"

    totalRoomsSearched = 0

    searchedTemp = 0

    introduction()

    cheat = False
    

    while programRun:

        if keysLeft == 0:
            programRun = False
            print("\nCongradulations! All the keys have been found.")
            print("You use the three keys to unlock the front door and exit the house\n")
            print("You searched a total of ", totalRoomsSearched , " rooms to find all the keys")

        elif cheat == True:

            print("\n")
            print("Cheat Entered : Show Answers")
            print('Answers: Top Floor = ' , topLocation, " / Main Floor =  " ,mainLocation, " / Basement = " ,basementLocation, '\n')
            cheat = False

        

        elif currentFloor == "Main Floor":

            keyMain , currentFloor, addKey, searchedTemp, cheat = floor(mainFloor, mainLocation, keyMain)

            totalKeys = totalKeys + addKey

            keysLeft = keysLeft - addKey

            totalRoomsSearched = totalRoomsSearched + searchedTemp
            searchedTemp = 0

            if addKey == 1:
                print("\nYou found a key!")

            
            print("Keys found = ", totalKeys, "\tKeys left = ", keysLeft, '\n')
            print("Total rooms searched = ", totalRoomsSearched, "\n")



        elif currentFloor == "Upstairs":

            keyTop , currentFloor, addKey, searchedTemp, cheat = floor(topFloor, topLocation, keyTop)
        
            totalKeys = totalKeys + addKey

            keysLeft = keysLeft - addKey

            totalRoomsSearched = totalRoomsSearched + searchedTemp
            searchedTemp = 0

            if addKey == 1:
                print("\nYou found a key!")

            print("Keys found = ", totalKeys, "\tKeys left = ", keysLeft, '\n')
            print("Total rooms searched = ", totalRoomsSearched, "\n")


            print("Current Location: " , currentFloor)

        elif currentFloor == "Basement":

            keyBasement , currentFloor, addKey, searchedTemp, cheat = floor(basementFloor, basementLocation, keyBasement)

            totalKeys = totalKeys + addKey

            keysLeft = keysLeft - addKey

            totalRoomsSearched = totalRoomsSearched + searchedTemp
            searchedTemp = 0

            if addKey == 1:
                print("\nYou found a key!")
                
            print("Keys found = ", totalKeys, "\tKeys left = ", keysLeft, '\n')
            print("Total rooms searched = ", totalRoomsSearched, "\n")


            print("Current Location: " , currentFloor)

        elif currentFloor == "Exit":
            programRun = False



        else:
            print("Error has Occured {REF 001}")
            programRun = False

   

main()