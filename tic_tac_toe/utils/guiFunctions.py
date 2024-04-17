def print_board(board, current_player, selectedCell, winning_cells=None):
    def checkIfWinningCell(x,y):
        isWinningCell = False
        for cell in winning_cells:
            winning_x = cell[0]
            winning_y = cell[1]
            if winning_x == x and winning_y == y:
                isWinningCell = True
        return isWinningCell
                

    if winning_cells == None:
        print("Current player: " + current_player +"\n")
        for row_idx in range(len(board)):
            print("-" * (7 * len(board[row_idx]) + 1))  
            for _ in range(3):  
                for col_idx in range(len(board[row_idx])):
                    if(selectedCell["y"] == row_idx and selectedCell["x"] == col_idx):
                        if((board[row_idx][col_idx] != "") and _ == 1):
                            print("|\033[7m"," ", board[row_idx][col_idx], end="  \033[0m") 
                        elif(board[row_idx][col_idx] != ""):
                            print("|\033[7m","   ", end="  \033[0m") 
                        else: 
                            print("|\033[7m","  ", board[row_idx][col_idx], end="  \033[0m") 
                    elif((board[row_idx][col_idx] != "") and _ == 1):
                        print("|  ", board[row_idx][col_idx], end="  ") 
                    elif(board[row_idx][col_idx] != ""):
                        print("|   ", end="   ") 
                    elif(not (selectedCell["y"] == row_idx and selectedCell["x"] == col_idx)):
                        print("|", end="      ") 
                print("|") 
        print("-" * (7 * len(board[row_idx]) + 1)) 
    else:
        for row_idx in range(len(board)):
            print("-" * (7 * len(board[row_idx]) + 1))  
            for _ in range(3):  
                for col_idx in range(len(board[row_idx])):
                    if checkIfWinningCell(row_idx, col_idx):
                        if((board[row_idx][col_idx] != "") and _ == 1):
                            print("|//",board[row_idx][col_idx], end="//") 
                        elif(board[row_idx][col_idx] != ""):
                            print("|//", end="////") 
                        else: 
                            print("|////", board[row_idx][col_idx], end="///")
                    else:
                        if(selectedCell["y"] == row_idx and selectedCell["x"] == col_idx):
                            if((board[row_idx][col_idx] != "") and _ == 1):
                                print("|\033[7m"," ", board[row_idx][col_idx], end="  \033[0m") 
                            elif(board[row_idx][col_idx] != ""):
                                print("|\033[7m","   ", end="  \033[0m") 
                            else: 
                                print("|\033[7m","  ", board[row_idx][col_idx], end="  \033[0m") 
                        elif((board[row_idx][col_idx] != "") and _ == 1):
                            print("|  ", board[row_idx][col_idx], end="  ") 
                        elif(board[row_idx][col_idx] != ""):
                            print("|   ", end="   ") 
                        elif(not (selectedCell["y"] == row_idx and selectedCell["x"] == col_idx)):
                            print("|", end="      ") 
                print("|") 
        print("-" * (7 * len(board[row_idx]) + 1)) 