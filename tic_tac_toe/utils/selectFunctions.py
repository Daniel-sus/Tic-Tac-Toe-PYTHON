# HELPER FUNCTIONS
def selectSymbol(player):
    while True:
        print(f"\nPlayer {player}: Select your symbol (only 1 character possible): ")
        player_input = input()
        if len(player_input) == 1:
            return player_input
        else:
            print("The input does not contain only one symbol")

def selectName(player):
    while True:
        print(f"\nPlayer {player+1}: Select your Name (from 1 to 10 characters): ")
        player_input = input()
        if len(player_input) >= 1 and len(player_input) <= 10:
            return player_input
        else:
            print("The name must be from 1 to 10 characters")


# MAIN FUNCTIONS
def selectQuantityOfPlayers():
    while True:
        print("\nHow many players do you want to play with?\n2 or 4")
        quantityOfPlayers = input()
        try: 
            quantityOfPlayersParsed = int(quantityOfPlayers)
            if quantityOfPlayersParsed == 2 or quantityOfPlayersParsed == 4:
                return quantityOfPlayersParsed
            else: 
                print("The quantity of players must be 2 or 4")
        except:
            print("The quantity of players must be 2 or 4 6")

def selectGridSize():
    while True:    
        print("\nChoose the size of the game?\nfrom 5x5 to 25x25")
        gridSize = input()
        try:
            gridSizeParsed = int(gridSize) 
            if gridSizeParsed >= 5 and gridSizeParsed <= 25:
                return gridSizeParsed
            else: 
                print("The size of the game must be from 5x5 to 25x25")
        except:
            print("The size of the game must be from 5x5 to 25x25")

def selectPlayersSymbols(player_names):
    playerSymbols = []
    for player in range(len(player_names)):
        playerSymbol = selectSymbol(player_names[player])
        playerSymbols.append(playerSymbol)
    return playerSymbols

def selectPlayersNames(num_players): 
    playersNames = []
    for player in range(num_players):
        playerName = selectName(player)
        playersNames.append(playerName)
    return playersNames