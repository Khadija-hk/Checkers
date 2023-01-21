''' This class contains functions the modify and display the board '''

# Import modules
# from game import *
from player1 import Player1
from player2 import Player2

# Start of the 'Board' class
class Board(Player1, Player2):  # Inherit from the parent classes

    # Class constructor
    def __init__(self):
        #Instantiate the parent classes
        Player1.__init__(self)
        Player2.__init__(self)

        # Initial board of the game 
        self.board = {  'A' : ['R','x','R','x','R','x','R','x'],
                        'B' : ['x','R','x','R','x','R','x','R'],
                        'C' : ['R','x','R','x','R','x','R','x'], 
                        'D' : ['B','R','B','R','B','R','B','R'],
                        'E' : ['R','B','R','B','R','B','R','B'] ,
                        'F' : ['o','R','o','R','o','R','o','R'],
                        'G' : ['R','o','R','o','R','o','R','o'],
                        'H' : ['o','R','o','R','o','R','o','R'] }

    #----------------------------------End of constructor---------------------------------------#   

    def modifyBoardPlayer1(self, name, start, end):

        ''' This function modifies the board according to the move entered by player 1
            It checks if the move is valid or not 
            It checks the piece type of the start location (to determine if it is a king move or not)
            It calls the display board function to show the modified board  '''
        
        # Split the start and end to thier respective row and column
        startRow , startCol = start.split('-')
        endRow , endCol = end.split('-')
        
        # Get the type of piece on the start location
        piece_type = self.checkPieceTypePlayer1(start)

        if(piece_type != 'invalid'):    # If the piece is normal or kinged, do:
            # Calls the valid move function to check if the move made is valid or not
            isValidMove = self.checkValidMovePlayer1(startRow,endRow,startCol,endCol,piece_type)  
            # Calls the empty square function to check if the end square in empty or not
            isEmptySquare = self.checkEmptySquare(endRow, endCol)   

            if(piece_type == 'x'):  # Check if it a jump for a normal piece
                isJump, jumpsqrRow, jumsqrCol, jumpSqr = self.isJumpPlayer1(startRow,endRow,startCol,endCol)    #Check if it is jump
            
            if(piece_type == 'X'):  # Check if it a jump for a kinged piece
                isJump, jumpsqrRow, jumsqrCol, jumpSqr = self.isJumpKingPlayer1(startRow,endRow,startCol,endCol)

            # If the move made is valid by player 1, modify the board and update the piece locations
            if(isValidMove and isEmptySquare): 
                self.updatePieceLoc_Player1(start,end,piece_type,endRow) #To update the piece in the player 1 piece list

                # This loop updates the board with the start and end location pieces
                for key, list in self.board.items():
                    if key == startRow.upper():
                        list[int(startCol) - 1] = 'B'   #Make the start location empty
                    if key == endRow.upper():
                        pieceList = [key for key, list in self.player1_pieces.items() if end in list] #To extract the piece type as key
                        piece = pieceList[0]    # To get the value only 
                        list[int(endCol) - 1] = piece  # Replace in the board

                # If the move made by the player was a jump 
                if(isJump):
                    self.decrement_count_Player2() #To decrement the count of the opponent player piece
                    self.removePiece_Player2(jumpSqr)   #To remove the piece which was jumped

                    # Loop the board to make the jump location of the piece empty
                    for key, list in self.board.items():
                        if key == jumpsqrRow.upper():
                            list[int(jumsqrCol) - 1] = 'B' 

                # After updating the pieces on the board, display the board
                self.displayBoard(self.fileName, name, 'Player 1', start, end)
            
            else:      # The move entered was illegal by the user
                print("\nThe move you have entered is invalid!")
                self.player1_Moves()

        else:   # The user has no piece on the start location, which makes the move invalid
            print("\nThe move you have entered is invalid!")
            self.player1_Moves()

    #-------------------------------------------------End of function------------------------------------------------#

    def modifyBoardPlayer2(self, name, start, end):

        ''' This function modifies the board according to the move entered by player 2
            It checks if the move is valid or not 
            It checks the piece type of the start location (to determine if it is a king move or not)
            It calls the display board function to show the modified board  '''

        # Split the start and end to thier respective row and column
        startRow , startCol = start.split('-')
        endRow , endCol = end.split('-')

        # Get the type of piece on the start location
        piece_type = self.checkPieceTypePlayer2(start)
        
        if(piece_type != 'invalid'):    # If the piece is normal or kinged, do:
            # Calls the valid move function to check if the move made is valid or not

            isValidMove = self.checkValidMovePlayer2(startRow,endRow,startCol,endCol,piece_type)   
            # Calls the empty square function to check if the end square in empty or not
            isEmptySquare = self.checkEmptySquare(endRow, endCol)

            if(piece_type == 'o'):  # Check if it a jump for a normal piece
                isJump, jumpsqrRow, jumsqrCol, jumpSqr = self.isJumpPlayer2(startRow,endRow,startCol,endCol)  

            if(piece_type == 'O'):  # Check if it a jump for a kinged piece
                isJump, jumpsqrRow, jumsqrCol, jumpSqr = self.isJumpKingPlayer2(startRow,endRow,startCol,endCol)
                
            # If the move made is valid by player , modify the board and update the piece locations
            if(isValidMove and isEmptySquare):  
                self.updatePieceLoc_Player2(start,end,piece_type,endRow) #To update the piece in the player 2 piece list
                
                # This loop updates the board with the start and end location pieces
                for key, list in self.board.items():
                    if key == startRow.upper():
                        list[int(startCol) - 1] = 'B'   #Make the start location empty
                    if key == endRow.upper():
                        pieceList = [key for key, list in self.player2_pieces.items() if end in list] #To extract the piece type as key
                        piece = pieceList[0]    # To get the value only 
                        list[int(endCol) - 1] = piece   # Replace it in the board

                # If the move made by the player was a jump 
                if(isJump):
                    self.decrement_count_Player1() #To decrement the count of the opponent player piece
                    self.removePiece_Player1(jumpSqr)   #To remove the piece which was jumped

                    # Loop the board to make the jump location of the piece empty
                    for key, list in self.board.items():
                        if key == jumpsqrRow.upper():
                            list[int(jumsqrCol) - 1] = 'B'  

                # After updating the pieces on the board, display the board
                self.displayBoard(self.fileName, name, 'Player 2', start, end)
            
            else:    # The move entered was illegal by the user
                print("\nThe move you have entered is invalid!")
                self.player2_Moves()

        else:   # The user has no piece on the start location, which makes the move invalid
            print("\nThe move you have entered is invalid!")
            self.player2_Moves()
    
    #-------------------------------------------------End of function------------------------------------------------#

    def checkEmptySquare(self, endRow, endCol):

        ''' This function checks if the square is empty or not, by checking the board location  '''

        #Loop through the board and find if the landing square (row and col) are marked empty - 'B'
        for key, list in self.board.items():
            if key == endRow.upper():
                if list[int(endCol)-1] == 'B':
                    return True # If empty
                else:
                    return False    # If not empty

    #-------------------------------------------------End of function------------------------------------------------#

    def displayBoard(self,fileName, name, playerNum, start, end):

        ''' This function is for rendering the board - on the console and write on the file
            It takes in 4 arguments (name of the player, which number of player is it, start square and end square)
            The filename is also passed as an argument 
            If it is at the start of the game, only the board is displayed
            Else, the name of the player along with the move information is also displayed (in the file)    '''
        
        # Print on the console
        print("    ",end = '')
        col_List = [1,2,3,4,5,6,7,8]
        for col in col_List:
            print("  " + str(col) + "  ", end=' ')
        print("\n")

        for row, col in self.board.items():
            print(row + '|', end=' ')
            for val in col:
                print("  " + val + "  ", end=' ')
            
            print("\n----------------------------------------------------")

        # Write in the file - 'append' mode
        with open(fileName,'a') as f:

            if(name != ""):
                print(f"\n\n{playerNum}: {name} moves {start} to {end}\n", file = f)

            print("    ",end = '', file = f)
            
            for col in col_List:
                print("  " + str(col) + "  ", end=' ',file = f)
            print("\n",file = f)

            for row, col in self.board.items():
                print(row + '|', end=' ',file = f)
                for val in col:
                    print("  " + val + "  ", end=' ',file = f)
                
                print("\n----------------------------------------------------",file = f)

    #-------------------------------------------------End of function------------------------------------------------#

#---------------------------------------------------------End of class------------------------------------------------------#
