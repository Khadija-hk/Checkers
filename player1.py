''' This class contains the variables and functions for the Player 1 pieces '''

# Import the modules needed
# from board import *
# from game import *

# Start of the 'Player1' class
class Player1:

    #A dictionary of lists to store the valid moves for a normal piece for player 1
    validMoves = { '1': ['2','3'],
                    '2': ['1','3','4'],
                    '3': ['1','2','4','5'],
                    '4': ['2','3','5','6'],
                    '5': ['3','4','6','7'],
                    '6': ['4','5','7','8'],
                    '7': ['5','6','8'],
                    '8': ['6','7']}
    
    validKingMoves = {  'a' : ['b','c'],
                        'b' : ['a','c','d'],
                        'c' : ['a','b','d','e'],
                        'd' : ['b','c','e','f'],
                        'e' : ['c','d','f','g'],
                        'f' :['d','e','g','h'],
                        'g' :['e','f','h'],
                        'h' : ['f','g'] }

    kingRow = 'h'

    # Class constructor
    def __init__(self):
        #List of pieces initially on the board along with the type
        self.player1_pieces = {'x': ['a-2', 'a-4', 'a-6', 'a-8',
                                        'b-1', 'b-3', 'b-5', 'b-7',
                                            'c-2', 'c-4', 'c-6', 'c-8'],
                                'X' : []}

        # Count of the player 1 pieces on the board
        self.count_player1Pieces = 12

    #----------------------------------End of constructor---------------------------------------#  

    def checkValidMovePlayer1(self,startRow,endRow,startCol,endCol,piece_type):
        
        ''' This function checks is the piece move is valid or not 
            It is divided into two parts - valid move for normal piece and king piece  '''

        if(startRow != endRow and startCol != endCol):  # If the player does not move in the same row or column
            if(piece_type == 'x'):  # If it is normal piece
                newEndRow = chr(ord(startRow) + 2)    # To check the max row it can go
                
                if(endRow > startRow and endRow <= newEndRow ):   # If the player moves legally
                    for key, list in Player1.validMoves.items():    # Check if the player moves in the correct column 
                        if key == startCol:
                            if endCol in list:
                                return True
                            else:
                                return False
                else:
                    return False
                
            # If it is a kinged piece - it can move in both directions
            else:
                isValidKingRow = self.validateRow(startRow, endRow) #seperate functions to calculate the valid king rows and columns
                isValidKingCol = self.validateCol(startCol, endCol)

                if(isValidKingRow and isValidKingCol):
                    return True
                else:
                    return False
        else:
            return False
    
    #-------------------------------------------------End of function------------------------------------------------#

    def isJumpPlayer1(self,startRow,endRow,startCol,endCol):
        
        ''' This function is for checking if the player made a jump
            It calculates the jump square 
            It checks if the jump is in the correct direction
            Also, the jump square should have a piece from the opponent  '''

        newEndRow = chr(ord(startRow) + 2)    # To check the max col it can go

        # Initailize the jump square variables
        jumpsqrRow = ""
        jumsqrCol = ""
        jumpSqr = ""

        if endRow == newEndRow:   # It is a jump - it moves two squares

            # Calculate the jump square inbetween
            jumpsqrRow = chr(ord(startRow) + 1)     # Calculate the row inbetween
            if((int(startCol) - 1) > int(endCol)):    # Calculate the column inbetween
                jumsqrCol = str(int(startCol) - 1)
            else:
                jumsqrCol = str(int(startCol) + 1)

            jumpSqr = jumpsqrRow + '-' + jumsqrCol  # Get the jump square 
            
            #To check if the piece you are jumping on is the opposite piece
            for key, list in self.player2_pieces.items():   
                if(key == 'o'):
                    if jumpSqr in list:
                        return True, jumpsqrRow, jumsqrCol, jumpSqr
                if(key == 'O'):
                    if jumpSqr in list:
                        return True, jumpsqrRow, jumsqrCol, jumpSqr
                    else:
                        return False, jumpsqrRow, jumsqrCol, jumpSqr
        else:
            return False, jumpsqrRow, jumsqrCol, jumpSqr
    
    #-------------------------------------------------End of function------------------------------------------------#

    def isJumpKingPlayer1(self,startRow,endRow,startCol,endCol):
        
        ''' This function is for checking if the king made a valid jump or not 
            It does the normal checks for jump but checks in the other direction too  '''

        # Initailize the jump square variables
        jumpsqrRow = ""
        jumsqrCol = ""
        jumpSqr = ""

        if(ord(startRow)<ord(endRow)):  # If the jump is forward
            newEndRow = chr(ord(startRow) + 2)    #To check the max col it can go
            
            if endRow == newEndRow:   #It is a jump

                #Calculate the square inbetween
                jumpsqrRow = chr(ord(startRow) + 1) # Calculate the row inbetween
                if((int(startCol) - 1) > int(endCol)):    # Calculate the column inbetween
                    jumsqrCol = str(int(startCol) - 1)
                else:
                    jumsqrCol = str(int(startCol) + 1)

                jumpSqr = jumpsqrRow + '-' + jumsqrCol  # Get the jump square 
                
                #To check if the piece you are jumping on is the opposite piece
                for key, list in self.player2_pieces.items():  
                    if(key == 'o'):
                        if jumpSqr in list:
                            return True, jumpsqrRow, jumsqrCol, jumpSqr
                    if(key == 'O'):
                        if jumpSqr in list:
                            return True, jumpsqrRow, jumsqrCol, jumpSqr
                        else:
                            return False, jumpsqrRow, jumsqrCol, jumpSqr
            else:
                return False, jumpsqrRow, jumsqrCol, jumpSqr
            
        if(ord(startRow)>ord(endRow)):  # If the jump is backward
            newEndRow = chr(ord(startRow) - 2)    #To check the max col it can go

            if endRow == newEndRow:   #It is a jump
                #Calculate the square inbetween
                jumpsqrRow = chr(ord(startRow) - 1) # Calculate the row inbetween
                if((int(startCol) - 1) > int(endCol)):    # Calculate the column inbetween
                    jumsqrCol = str(int(startCol) - 1)
                else:
                    jumsqrCol = str(int(startCol) + 1)

                jumpSqr = jumpsqrRow + '-' + jumsqrCol  # Get the jump square 
                
                #To check if the piece you are jumping on is the opposite piece
                for key, list in self.player2_pieces.items():   
                    if(key == 'o'):
                        if jumpSqr in list:
                            return True, jumpsqrRow, jumsqrCol, jumpSqr
                    if(key == 'O'):
                        if jumpSqr in list:
                            return True, jumpsqrRow, jumsqrCol, jumpSqr
                        else:
                            return False, jumpsqrRow, jumsqrCol, jumpSqr
            else:
                return False, jumpsqrRow, jumsqrCol, jumpSqr

    #-------------------------------------------------End of function------------------------------------------------#

    def updatePieceLoc_Player1(self,start,end,piece_type,endRow):

        ''' This function updates the start and end location in the board
            If has three checks: if the piece is normal, if the piece is kinged, if the piece is a king.  '''
        
        # If the piece has been kinged
        if(piece_type == 'x' and endRow == Player1.kingRow):
            for key, list in self.player1_pieces.items():
                if key == 'x':
                    if start in list:
                        list.remove(start)  # Remove the piece from the start location
                if key == 'X':
                    list.append(end)    # Add a king piece in the end location            

        # If it is normal piece
        if(piece_type == 'x'):
            for key, list in self.player1_pieces.items():
                if key == 'x':
                    if start in list:
                        list.remove(start)  # Remove the piece from the start
                        list.append(end)    # Add the piece to the end

        # If it is a kinged piece
        if(piece_type == 'X'):
            for key, list in self.player1_pieces.items():
                if key == 'X':
                    if start in list:
                        list.remove(start)  # Remove the piece from the start
                        list.append(end)    # Add the piece to the end

    #-------------------------------------------------End of function------------------------------------------------#

    def decrement_count_Player1(self):

        ''' This function simply decrements the count of pieces on the board '''
        self.count_player1Pieces -= 1
    
    #-------------------------------------------------End of function------------------------------------------------#

    def removePiece_Player1(self,jumpedPiece):

        ''' This function only removes a piece from the player 1 pieces (when it has been jumped on) '''
        for key, list in self.player1_pieces.items():
            if jumpedPiece in list:
                list.remove(jumpedPiece)
    #-------------------------------------------------End of function------------------------------------------------#

    def checkPieceTypePlayer1(self,piece):
        
        ''' This function is to check what is the piece type by traversing the list and returning the key '''

        for key, list in self.player1_pieces.items():   
            if key == 'x':
                if piece in list:
                    return key
            if key == 'X':
                if piece in list:
                    return key
            
        return 'invalid'    # If the piece given to check is neither a normal piece nor a king

    #-------------------------------------------------End of function------------------------------------------------#

    def validateRow(self,startRow, endRow):
        
        ''' This function is to check if the king is moving in the valid row or not,
            by traversing the valid moves dictionary '''

        for key, list in Player1.validKingMoves.items():
            if key == startRow:
                if endRow in list:
                    return True
                else:
                    return False
    #-------------------------------------------------End of function------------------------------------------------#

    def validateCol(self,startCol, endCol):
        
        ''' This function is to check if the king is moving in the valid column or not,
            by traversing the valid moves dictionary '''

        for key, list in Player1.validMoves.items():
            if key == startCol:
                if endCol in list:
                    return True
                else:
                    return False
    
    #-------------------------------------------------End of function------------------------------------------------#

#-------------------------------------------------End of class------------------------------------------------#
    






                

    






